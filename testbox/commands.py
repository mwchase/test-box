import os
import subprocess
import sys


def python_module(args):
    subprocess.call((sys.executable, '-m') + args)


COVER = 'coverage'
PYTEST = 'py.test'


def initial_package(package):
    python_module((COVER, 'run', '--source={}'.format(package),
                   '{}/__init__.py'.format(package)))


def erase():
    python_module((COVER, 'erase'))


def html():
    python_module((COVER, 'html'))


def dotted_module(module):
    return '.'.join(module)


def slashed_module(module):
    return os.sep.join(module)


def run(package, module, test='test', results='results',
        aggregate='aggregate-results.xml'):
    python_module(COVER, 'run', '-a',
                  '--source={}.{}'.format(package, dotted_module(module)),
                  '-m', PYTEST, '--junit-xml={}/{}.xml'.format(
                      results, dotted_module(module)),
                  '{}/{}'.format(test, slashed_module(module)))
