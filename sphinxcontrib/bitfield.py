from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import flag
from bit_field import render, jsonml_stringify
from json import loads
from hashlib import sha1
from os.path import join
from sphinx.errors import ExtensionError
from shlex import split


class bitfield(nodes.General, nodes.Element):
    pass


def set_bitfield_options(node: bitfield):
    """
    Set boolean flags based on user-provided options
    """
    node.options = node.attributes.get('options', {})
    node.options['compact'] = 'compact' in node.options
    node.options['hflip'] = 'hflip' in node.options
    node.options['vflip'] = 'vflip' in node.options
    node.options['uneven'] = 'uneven' in node.options


def visit_bitfield_html(self, node):
    set_bitfield_options(node)
    self.body.append(
        jsonml_stringify(
            render(
                loads(' '.join(node.rawsource)),
                **node.options
            )
        )
    )


def visit_bitfield_latex(self, node):
    try:
        from cairosvg import svg2pdf
    except ModuleNotFoundError as e:
        raise ExtensionError('Please install optional requirements to enable '
                             'LateX support:\n'
                             '  pip install sphinxcontrib-bitfield[LaTeX]', e)

    set_bitfield_options(node)
    svg = jsonml_stringify(
        render(
            loads(' '.join(node.rawsource)),
            **node.options
        )
    )
    hashkey = str(node.options) + str(node.rawsource)
    fname = 'bitfield-{}.pdf'.format(sha1(hashkey.encode()).hexdigest())
    outfn = join(self.builder.outdir, self.builder.imagedir, fname)
    svg2pdf(bytestring=svg, write_to=outfn)

    self.body.append(r'\sphinxincludegraphics[]{{{}}}'.format(fname))


def depart_bitfield(self, node):
    pass


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
        return [bitfield(self.content, options=self.options)]


def setup(app):
    app.add_node(bitfield,
                 html=(visit_bitfield_html, depart_bitfield),
                 latex=(visit_bitfield_latex, depart_bitfield))
    app.add_directive('bitfield', BitfieldDirective)
