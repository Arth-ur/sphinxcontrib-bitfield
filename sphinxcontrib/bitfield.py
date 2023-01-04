from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import flag
from bit_field import render, jsonml_stringify
from json import loads
from hashlib import sha1
from os.path import join
from sphinx.errors import ExtensionError


class bitfield(nodes.General, nodes.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.options = dict(kwargs['options'])
        self.options['compact'] = 'compact' in self.options
        self.options['hflip'] = 'hflip' in self.options
        self.options['vflip'] = 'vflip' in self.options


def visit_bitfield_html(self, node):
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


class BitfieldDirective(Directive):
    has_content = True
    option_spec = {
        'vspace': int,
        'hspace': int,
        'lanes': int,
        'bits': int,
        'fontsize': int,
        'fontfamily': str,
        'fontweight': str,
        'compact': flag,
        'hflip': flag,
        'vflip': flag,
    }

    def run(self):
        return [bitfield(self.content, options=self.options)]


def setup(app):
    app.add_node(bitfield,
                 html=(visit_bitfield_html, depart_bitfield),
                 latex=(visit_bitfield_latex, depart_bitfield))
    app.add_directive('bitfield', BitfieldDirective)
