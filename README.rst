sphinxcontrib-bitfield
======================


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

.. raw:: html

    <svg width="649" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 649 165" height="165"><g transform="translate(4.5, 80.5)"><g stroke-width="1" stroke="black" stroke-linecap="round" transform="translate(0, 20.0)"><line x2="640"></line><line y2="40.0"></line><line x1="0" y2="40.0" y1="40.0" x2="640"></line><line x1="640.0" y2="40.0" x2="640.0"></line><line x1="600.0" y2="5.0" x2="600.0"></line><line x1="600.0" y2="5.0" x2="600.0"></line><line x1="560.0" y2="5.0" x2="560.0"></line><line x1="560.0" y2="5.0" x2="560.0"></line><line x1="520.0" y2="5.0" x2="520.0"></line><line x1="520.0" y2="5.0" x2="520.0"></line><line x1="480.0" y2="5.0" x2="480.0"></line><line x1="480.0" y2="5.0" x2="480.0"></line><line x1="440.0" y2="5.0" x2="440.0"></line><line x1="440.0" y2="5.0" x2="440.0"></line><line x1="400.0" y2="5.0" x2="400.0"></line><line x1="400.0" y2="5.0" x2="400.0"></line><line x1="360.0" y2="5.0" x2="360.0"></line><line x1="360.0" y2="5.0" x2="360.0"></line><line x1="320.0" y2="40.0" x2="320.0"></line><line x1="280.0" y2="5.0" x2="280.0"></line><line x1="280.0" y2="5.0" x2="280.0"></line><line x1="240.0" y2="5.0" x2="240.0"></line><line x1="240.0" y2="5.0" x2="240.0"></line><line x1="200.0" y2="5.0" x2="200.0"></line><line x1="200.0" y2="5.0" x2="200.0"></line><line x1="160.0" y2="5.0" x2="160.0"></line><line x1="160.0" y2="5.0" x2="160.0"></line><line x1="120.0" y2="5.0" x2="120.0"></line><line x1="120.0" y2="5.0" x2="120.0"></line><line x1="80.0" y2="5.0" x2="80.0"></line><line x1="80.0" y2="5.0" x2="80.0"></line><line x1="40.0" y2="40.0" x2="40.0"></line></g><g text-anchor="middle"><g><g transform="translate(0, 20.0)"><rect width="280.0" height="40.0" x="40.0" style="fill-opacity:0.1" y="0"></rect><rect width="40.0" height="40.0" x="0.0" style="fill-opacity:0.1;fill:hsl(170,100%,50%)" y="0"></rect></g><g transform="translate(20.0, 16.0)"><text font-weight="normal" x="600.0" font-family="sans-serif" font-size="14">0</text><text font-weight="normal" x="320.0" font-family="sans-serif" font-size="14">7</text><text font-weight="normal" x="280.0" font-family="sans-serif" font-size="14">8</text><text font-weight="normal" x="40.0" font-family="sans-serif" font-size="14">14</text><text font-weight="normal" x="0.0" font-family="sans-serif" font-size="14">15</text></g><g transform="translate(20.0, 44.0)"><text font-weight="normal" x="460.0" font-family="sans-serif" font-size="14"><tspan>IPO</tspan></text><text font-weight="normal" x="0.0" font-family="sans-serif" font-size="14"><tspan>BRK</tspan></text></g><g transform="translate(20.0, 80)"><text font-weight="normal" x="460.0" font-family="sans-serif" font-size="14"><tspan>RO</tspan></text><text font-weight="normal" x="0.0" font-family="sans-serif" font-size="14"><tspan>RW</tspan></text></g></g></g></g><g transform="translate(4.5, 0.5)"><g stroke-width="1" stroke="black" stroke-linecap="round" transform="translate(0, 20.0)"><line x2="640"></line><line y2="40.0"></line><line x1="0" y2="40.0" y1="40.0" x2="640"></line><line x1="640.0" y2="40.0" x2="640.0"></line><line x1="600.0" y2="5.0" x2="600.0"></line><line x1="600.0" y2="5.0" x2="600.0"></line><line x1="560.0" y2="5.0" x2="560.0"></line><line x1="560.0" y2="5.0" x2="560.0"></line><line x1="520.0" y2="5.0" x2="520.0"></line><line x1="520.0" y2="5.0" x2="520.0"></line><line x1="480.0" y2="40.0" x2="480.0"></line><line x1="440.0" y2="40.0" x2="440.0"></line><line x1="400.0" y2="5.0" x2="400.0"></line><line x1="400.0" y2="5.0" x2="400.0"></line><line x1="360.0" y2="5.0" x2="360.0"></line><line x1="360.0" y2="5.0" x2="360.0"></line><line x1="320.0" y2="40.0" x2="320.0"></line><line x1="280.0" y2="5.0" x2="280.0"></line><line x1="280.0" y2="5.0" x2="280.0"></line><line x1="240.0" y2="5.0" x2="240.0"></line><line x1="240.0" y2="5.0" x2="240.0"></line><line x1="200.0" y2="5.0" x2="200.0"></line><line x1="200.0" y2="5.0" x2="200.0"></line><line x1="160.0" y2="5.0" x2="160.0"></line><line x1="160.0" y2="5.0" x2="160.0"></line><line x1="120.0" y2="5.0" x2="120.0"></line><line x1="120.0" y2="5.0" x2="120.0"></line><line x1="80.0" y2="5.0" x2="80.0"></line><line x1="80.0" y2="5.0" x2="80.0"></line><line x1="40.0" y2="5.0" x2="40.0"></line><line x1="40.0" y2="5.0" x2="40.0"></line></g><g text-anchor="middle"><g><g transform="translate(0, 20.0)"><rect width="160.0" height="40.0" x="480.0" style="fill-opacity:0.1;fill:hsl(170,100%,50%)" y="0"></rect><rect width="320.0" height="40.0" x="0.0" style="fill-opacity:0.1" y="0"></rect></g><g transform="translate(20.0, 16.0)"><text font-weight="normal" x="600.0" font-family="sans-serif" font-size="14">16</text><text font-weight="normal" x="480.0" font-family="sans-serif" font-size="14">19</text><text font-weight="normal" x="440.0" font-family="sans-serif" font-size="14">20</text><text font-weight="normal" x="400.0" font-family="sans-serif" font-size="14">21</text><text font-weight="normal" x="320.0" font-family="sans-serif" font-size="14">23</text><text font-weight="normal" x="280.0" font-family="sans-serif" font-size="14">24</text><text font-weight="normal" x="0.0" font-family="sans-serif" font-size="14">31</text></g><g transform="translate(20.0, 44.0)"><text font-weight="normal" x="540.0" font-family="sans-serif" font-size="14"><tspan>BRK</tspan></text><text font-weight="normal" x="440.0" font-family="sans-serif" font-size="14"><tspan>CPK</tspan></text><text font-weight="normal" x="360.0" font-family="sans-serif" font-size="14"><tspan>Clear</tspan></text></g><g transform="translate(20.0, 80)"><text font-weight="normal" x="540.0" font-family="sans-serif" font-size="14"><tspan>RW</tspan></text></g></g></g></g></svg>


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

.. raw:: html

    <svg width="649" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 649 85" height="85"><g transform="translate(4.5, 0.5)"><g stroke-width="1" stroke="black" stroke-linecap="round" transform="translate(0, 20.0)"><line x2="640"></line><line y2="40.0"></line><line x1="0" y2="40.0" y1="40.0" x2="640"></line><line x1="640.0" y2="40.0" x2="640.0"></line><line x1="560.0" y2="40.0" x2="560.0"></line><line x1="480.0" y2="40.0" x2="480.0"></line><line x1="400.0" y2="40.0" x2="400.0"></line><line x1="320.0" y2="40.0" x2="320.0"></line><line x1="240.0" y2="40.0" x2="240.0"></line><line x1="160.0" y2="40.0" x2="160.0"></line><line x1="80.0" y2="40.0" x2="80.0"></line></g><g text-anchor="middle"><g><g transform="translate(0, 20.0)"></g><g transform="translate(40.0, 16.0)"><text font-weight="normal" x="560.0" font-family="sans-serif" font-size="14">0</text><text font-weight="normal" x="480.0" font-family="sans-serif" font-size="14">1</text><text font-weight="normal" x="400.0" font-family="sans-serif" font-size="14">2</text><text font-weight="normal" x="320.0" font-family="sans-serif" font-size="14">3</text><text font-weight="normal" x="240.0" font-family="sans-serif" font-size="14">4</text><text font-weight="normal" x="160.0" font-family="sans-serif" font-size="14">5</text><text font-weight="normal" x="80.0" font-family="sans-serif" font-size="14">6</text><text font-weight="normal" x="0.0" font-family="sans-serif" font-size="14">7</text></g><g transform="translate(40.0, 44.0)"><text font-weight="normal" x="560.0" font-family="sans-serif" font-size="14"><tspan>C</tspan></text><text font-weight="normal" x="480.0" font-family="sans-serif" font-size="14"><tspan>Z</tspan></text><text font-weight="normal" x="400.0" font-family="sans-serif" font-size="14"><tspan>N</tspan></text><text font-weight="normal" x="320.0" font-family="sans-serif" font-size="14"><tspan>V</tspan></text><text font-weight="normal" x="240.0" font-family="sans-serif" font-size="14"><tspan>S</tspan></text><text font-weight="normal" x="160.0" font-family="sans-serif" font-size="14"><tspan>H</tspan></text><text font-weight="normal" x="80.0" font-family="sans-serif" font-size="14"><tspan>T</tspan></text><text font-weight="normal" x="0.0" font-family="sans-serif" font-size="14"><tspan>I</tspan></text></g><g transform="translate(40.0, 80)"></g></g></g></g></svg>

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

.. raw:: html

    <svg width="649" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 649 85" height="85"><g transform="translate(4.5, 0.5)"><g stroke-width="1" stroke="black" stroke-linecap="round" transform="translate(0, 20.0)"><line x2="640"></line><line y2="40.0"></line><line x1="0" y2="40.0" y1="40.0" x2="640"></line><line x1="640.0" y2="40.0" x2="640.0"></line><line x1="620.0" y2="5.0" x2="620.0"></line><line x1="620.0" y2="5.0" x2="620.0"></line><line x1="600.0" y2="5.0" x2="600.0"></line><line x1="600.0" y2="5.0" x2="600.0"></line><line x1="580.0" y2="5.0" x2="580.0"></line><line x1="580.0" y2="5.0" x2="580.0"></line><line x1="560.0" y2="5.0" x2="560.0"></line><line x1="560.0" y2="5.0" x2="560.0"></line><line x1="540.0" y2="40.0" x2="540.0"></line><line x1="520.0" y2="40.0" x2="520.0"></line><line x1="500.0" y2="40.0" x2="500.0"></line><line x1="480.0" y2="40.0" x2="480.0"></line><line x1="460.0" y2="40.0" x2="460.0"></line><line x1="440.0" y2="40.0" x2="440.0"></line><line x1="420.0" y2="5.0" x2="420.0"></line><line x1="420.0" y2="5.0" x2="420.0"></line><line x1="400.0" y2="5.0" x2="400.0"></line><line x1="400.0" y2="5.0" x2="400.0"></line><line x1="380.0" y2="5.0" x2="380.0"></line><line x1="380.0" y2="5.0" x2="380.0"></line><line x1="360.0" y2="5.0" x2="360.0"></line><line x1="360.0" y2="5.0" x2="360.0"></line><line x1="340.0" y2="5.0" x2="340.0"></line><line x1="340.0" y2="5.0" x2="340.0"></line><line x1="320.0" y2="40.0" x2="320.0"></line><line x1="300.0" y2="5.0" x2="300.0"></line><line x1="300.0" y2="5.0" x2="300.0"></line><line x1="280.0" y2="5.0" x2="280.0"></line><line x1="280.0" y2="5.0" x2="280.0"></line><line x1="260.0" y2="5.0" x2="260.0"></line><line x1="260.0" y2="5.0" x2="260.0"></line><line x1="240.0" y2="40.0" x2="240.0"></line><line x1="220.0" y2="5.0" x2="220.0"></line><line x1="220.0" y2="5.0" x2="220.0"></line><line x1="200.0" y2="5.0" x2="200.0"></line><line x1="200.0" y2="5.0" x2="200.0"></line><line x1="180.0" y2="5.0" x2="180.0"></line><line x1="180.0" y2="5.0" x2="180.0"></line><line x1="160.0" y2="40.0" x2="160.0"></line><line x1="140.0" y2="40.0" x2="140.0"></line><line x1="120.0" y2="5.0" x2="120.0"></line><line x1="120.0" y2="5.0" x2="120.0"></line><line x1="100.0" y2="40.0" x2="100.0"></line><line x1="80.0" y2="40.0" x2="80.0"></line><line x1="60.0" y2="40.0" x2="60.0"></line><line x1="40.0" y2="40.0" x2="40.0"></line><line x1="20.0" y2="40.0" x2="20.0"></line></g><g text-anchor="middle"><g><g transform="translate(0, 20.0)"><rect width="120.0" height="40.0" x="320.0" style="fill-opacity:0.1;fill:hsl(0,100%,50%)" y="0"></rect><rect width="80.0" height="40.0" x="160.0" style="fill-opacity:0.1" y="0"></rect><rect width="40.0" height="40.0" x="100.0" style="fill-opacity:0.1;fill:hsl(0,100%,50%)" y="0"></rect></g><g transform="translate(10.0, 16.0)"><text font-weight="normal" x="620.0" font-family="sans-serif" font-size="14">0</text><text font-weight="normal" x="540.0" font-family="sans-serif" font-size="14">4</text><text font-weight="normal" x="520.0" font-family="sans-serif" font-size="14">5</text><text font-weight="normal" x="500.0" font-family="sans-serif" font-size="14">6</text><text font-weight="normal" x="480.0" font-family="sans-serif" font-size="14">7</text><text font-weight="normal" x="460.0" font-family="sans-serif" font-size="14">8</text><text font-weight="normal" x="440.0" font-family="sans-serif" font-size="14">9</text><text font-weight="normal" x="420.0" font-family="sans-serif" font-size="14">10</text><text font-weight="normal" x="320.0" font-family="sans-serif" font-size="14">15</text><text font-weight="normal" x="300.0" font-family="sans-serif" font-size="14">16</text><text font-weight="normal" x="240.0" font-family="sans-serif" font-size="14">19</text><text font-weight="normal" x="220.0" font-family="sans-serif" font-size="14">20</text><text font-weight="normal" x="160.0" font-family="sans-serif" font-size="14">23</text><text font-weight="normal" x="140.0" font-family="sans-serif" font-size="14">24</text><text font-weight="normal" x="120.0" font-family="sans-serif" font-size="14">25</text><text font-weight="normal" x="100.0" font-family="sans-serif" font-size="14">26</text><text font-weight="normal" x="80.0" font-family="sans-serif" font-size="14">27</text><text font-weight="normal" x="60.0" font-family="sans-serif" font-size="14">28</text><text font-weight="normal" x="40.0" font-family="sans-serif" font-size="14">29</text><text font-weight="normal" x="20.0" font-family="sans-serif" font-size="14">30</text><text font-weight="normal" x="0.0" font-family="sans-serif" font-size="14">31</text></g><g transform="translate(10.0, 44.0)"><text font-weight="normal" x="580.0" font-family="sans-serif" font-size="14"><tspan>M</tspan></text><text font-weight="normal" x="520.0" font-family="sans-serif" font-size="14"><tspan>T</tspan></text><text font-weight="normal" x="500.0" font-family="sans-serif" font-size="14"><tspan>F</tspan></text><text font-weight="normal" x="480.0" font-family="sans-serif" font-size="14"><tspan>I</tspan></text><text font-weight="normal" x="460.0" font-family="sans-serif" font-size="14"><tspan>A</tspan></text><text font-weight="normal" x="440.0" font-family="sans-serif" font-size="14"><tspan>E</tspan></text><text font-weight="normal" x="370.0" font-family="sans-serif" font-size="14"><tspan>IT</tspan></text><text font-weight="normal" x="270.0" font-family="sans-serif" font-size="14"><tspan>GE</tspan></text><text font-weight="normal" x="140.0" font-family="sans-serif" font-size="14"><tspan>J</tspan></text><text font-weight="normal" x="110.0" font-family="sans-serif" font-size="14"><tspan>IT</tspan></text><text font-weight="normal" x="80.0" font-family="sans-serif" font-size="14"><tspan>Q</tspan></text><text font-weight="normal" x="60.0" font-family="sans-serif" font-size="14"><tspan>V</tspan></text><text font-weight="normal" x="40.0" font-family="sans-serif" font-size="14"><tspan>C</tspan></text><text font-weight="normal" x="20.0" font-family="sans-serif" font-size="14"><tspan>Z</tspan></text><text font-weight="normal" x="0.0" font-family="sans-serif" font-size="14"><tspan>N</tspan></text></g><g transform="translate(10.0, 80)"></g></g></g></g></svg>

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

