sphinxcontrib-bitfield
======================

A `Sphinx <https://www.sphinx-doc.org/en/master/>`_ extension to generate bit field diagrams with
the `bit_field <https://github.com/Arth-ur/bitfield>`_ Python package.

Installation
------------

::

    pip install sphinxcontrib-bitfield


To install with LaTeX support:

::

    pip install sphinxcontrib-bitfield[LaTeX]


Enable Extension
-----------------

Add `sphinxcontrib.bitfield` in `extensions` of `conf.py`::

    extensions = ['sphinxcontrib.bitfield']


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
    compact:
        compact rendering mode
    hflip:
        horizontal flip
    vflip:
        vertical flip

For more details, see the `bit_field <https://github.com/Arth-ur/bitfield>`_ package.
