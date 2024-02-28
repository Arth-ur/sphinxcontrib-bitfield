sphinxcontrib-bitfield
======================

A `Sphinx <https://www.sphinx-doc.org/en/master/>`_ extension to generate bit field diagrams with
the `bit_field <https://github.com/Arth-ur/bitfield>`_ Python package.

Installation
------------

::

    pip install sphinxcontrib-bitfield


Enable Extension
-----------------

Add `sphinxcontrib.bitfield` in `extensions` of `conf.py`::

    extensions = ['sphinxcontrib.bitfield']


To enable output with LaTeX support, add an image converter from SVG to PNG:

::

    extensions = ['sphinx.ext.imgconverter', 'sphinxcontrib.bitfield']


Usage
-----
Use directive `bitfield` with the description of the bitfield in JSON format::

    .. bitfield::
        :bits: 32
        :lanes: 2

            [
                { "name": "IPO",   "bits": 8, "attr": "RO" },
                {                  "bits": 7 },
                { "name": "BRK",   "bits": 5, "attr": "RW", "type": 4 },
                { "name": "CPK",   "bits": 1 },
                { "name": "Clear", "bits": 3 },
                { "bits": 8 }
            ]

.. image:: https://raw.githubusercontent.com/Arth-ur/bitfield/master/bit_field/test/alpha.svg?sanitize=true

The `bitfield` directive accepts the following options:
    vspace:
        vertical space - default 80
    hspace:
        horizontal space - default 640
    lanes:
        rectangle lanes - default 2
    bits:
        overall bitwidth - default 32
    fontfamily:
        default sans-serif
    fontweight:
        default normal
    fontsize:
        default 14
    strokewidth:
        default 1
    compact:
        compact rendering mode
    hflip:
        horizontal flip
    vflip:
        vertical flip
    uneven:
        uneven lanes
    trim:
        trim long bitfield names, must provide the horizontal space available for a single character
    legend:
        space separated list of name and type optionally enclosed in quotes
    caption:
        String caption for the bitfield. If specified, the bitfield will be rendered as a figure

For more details, see the `bit_field <https://github.com/Arth-ur/bitfield>`_ package.
