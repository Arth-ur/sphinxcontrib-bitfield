.. sphinxcontrib-bitfield documentation master file, created by
   sphinx-quickstart on Thu Jan  3 17:09:46 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to sphinxcontrib-bitfield's documentation!
==================================================


.. toctree::

Installation
------------

::

    pip install sphinxcontrib-bitfield


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


The `bitfield` directive accepts the following options:
    vspace:
        vertical space - default 80
    hspace:
        horizontal space - default 640
    lanes:
        rectangle lanes - default 2
    bits:
        overall bitwidth - default 32
    endianness:
        default `little`, non implemented
    fontfamily:
        default sans-serif
    fontweight:
        default normal
    fontsize:
        default 14

Examples
--------

.. bitfield::
    :bits: 8
    :lanes: 1
        
        [
            { "name": "C",   "bits": 1},
            { "name": "Z",   "bits": 1},
            { "name": "N",   "bits": 1},
            { "name": "V",   "bits": 1},
            { "name": "S",   "bits": 1},
            { "name": "H",   "bits": 1},
            { "name": "T",   "bits": 1},
            { "name": "I",   "bits": 1}
        ]


::

    .. bitfield::
        :bits: 8
        :lanes: 1
            
            [
                { "name": "C",   "bits": 1},
                { "name": "Z",   "bits": 1},
                { "name": "N",   "bits": 1},
                { "name": "V",   "bits": 1},
                { "name": "S",   "bits": 1},
                { "name": "H",   "bits": 1},
                { "name": "T",   "bits": 1},
                { "name": "I",   "bits": 1}
            ]

.. bitfield::
    :bits: 32
    :lanes: 1
        
        [
            { "name": "M",   "bits": 5},
            { "name": "T",   "bits": 1},
            { "name": "F",   "bits": 1},
            { "name": "I",   "bits": 1},
            { "name": "A",   "bits": 1},
            { "name": "E",   "bits": 1},
            { "name": "IT",  "bits": 6, "type": 2},
            { "name": "GE",  "bits": 4},
            {                "bits": 4},
            { "name": "J",   "bits": 1},
            { "name": "IT",  "bits": 2, "type": 2},
            { "name": "Q",   "bits": 1},
            { "name": "V",   "bits": 1},
            { "name": "C",   "bits": 1},
            { "name": "Z",   "bits": 1},
            { "name": "N",   "bits": 1}
        ]

::

    .. bitfield::
        :bits: 32
        :lanes: 1
            
            [
                { "name": "M",   "bits": 5},
                { "name": "T",   "bits": 1},
                { "name": "F",   "bits": 1},
                { "name": "I",   "bits": 1},
                { "name": "A",   "bits": 1},
                { "name": "E",   "bits": 1},
                { "name": "IT",  "bits": 6, "type": 2},
                { "name": "GE",  "bits": 4},
                {                "bits": 4},
                { "name": "J",   "bits": 1},
                { "name": "IT",  "bits": 2, "type": 2},
                { "name": "Q",   "bits": 1},
                { "name": "V",   "bits": 1},
                { "name": "C",   "bits": 1},
                { "name": "Z",   "bits": 1},
                { "name": "N",   "bits": 1}
            ]

