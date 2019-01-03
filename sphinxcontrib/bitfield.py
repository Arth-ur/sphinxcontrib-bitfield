from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import choice
from bit_field import render, jsonml_stringify
from json import loads


class bitfield(nodes.General, nodes.Element):
    def __init__(self, options, *args, **kwargs):
        super(bitfield, self).__init__(*args, **kwargs)
        self.options = options


def visit_bitfield(self, node):
    self.body.append(
        jsonml_stringify(
            render(
                loads(' '.join(node.rawsource)),
                **node.options
            )
        )
    )


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
        'endianness': lambda a: choice(a, ['big', 'little']),
        'fontfamily': str,
        'fontweight': str
    }

    def run(self):
        return [bitfield(self.options, self.content)]


def setup(app):
    app.add_node(bitfield,
                 html=(visit_bitfield, depart_bitfield))
    app.add_directive('bitfield', BitfieldDirective)
