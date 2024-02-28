from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives import flag
from bit_field import render, jsonml_stringify
from json import loads
from shlex import split
from base64 import b64encode
from sphinx import addnodes
from sphinx.util.nodes import set_source_info


def legend(s):
    x = split(s)
    return {k: v for k, v in zip(x[0::2], x[1::2])}


def figure_wrapper(directive, children, caption) -> nodes.figure:
    # based on the figure_wrapper method in sphinx.ext.graphviz
    # https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/graphviz.py
    figure_node = nodes.figure('', *children)

    inodes, messages = directive.state.inline_text(caption, directive.lineno)
    caption_node = nodes.caption(caption, '', *inodes)
    caption_node.extend(messages)
    set_source_info(directive, caption_node)
    figure_node += caption_node
    return figure_node


class BitfieldDirective(Directive):
    has_content = True
    option_spec = {
        'vspace': float,
        'hspace': float,
        'lanes': int,
        'bits': int,
        'fontsize': float,
        'fontfamily': str,
        'fontweight': str,
        'strokewidth': float,
        'compact': flag,
        'hflip': flag,
        'vflip': flag,
        'uneven': flag,
        'trim': float,
        'legend': legend,
        'caption': directives.unchanged,
    }

    def run(self):
        # remove 'caption' since its only used on the sphinx side and bit_field
        # doesnt recognize it
        caption = self.options.pop('caption', None)

        svg = jsonml_stringify(
            render(
                loads(' '.join(self.content)),
                **self.options
            )
        )

        uri = 'data:image/svg+xml;base64,' + b64encode(svg.encode()).decode()

        onlynode = addnodes.only(expr='latex')
        onlynode += nodes.image('', uri=uri)

        content = [nodes.raw('', svg, format='html'), onlynode]

        if caption is None:
            return content

        # wrap as a figure
        fig_node = figure_wrapper(self, content, caption)
        self.add_name(fig_node)
        return [fig_node]


def setup(app):
    app.add_directive('bitfield', BitfieldDirective)
