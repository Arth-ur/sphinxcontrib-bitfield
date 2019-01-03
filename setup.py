# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the bitfield Sphinx extension.

.. add description here ..
'''

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-bitfield',
    version='0.1',
    url='https://github.com/Arth-ur/sphinxcontrib-bitfield',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-bitfield',
    license='BSD',
    author='Arthur Gay',
    description='Sphinx "bitfield" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Sphinx :: Extension',
        #'Framework :: Sphinx :: Theme',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
