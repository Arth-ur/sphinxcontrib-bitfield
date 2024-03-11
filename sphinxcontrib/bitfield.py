from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import flag
from bit_field import render, jsonml_stringify
from json import loads
from shlex import split
from base64 import b64encode
from sphinx import addnodes


def legend(s):
    x = split(s)
    return {k: v for k, v in zip(x[0::2], x[1::2])}


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
    }

    def run(self):
        svg = jsonml_stringify(
            render(
                loads(' '.join(self.content)),
                **self.options
            )
        )

        uri = 'data:image/svg+xml;base64,' + b64encode(svg.encode()).decode()

        onlynode = addnodes.only(expr='latex')
        onlynode += nodes.image('', uri=uri)

        return [nodes.raw('', svg, format='html'), onlynode]


def setup(app):
    app.add_directive('bitfield', BitfieldDirective)
