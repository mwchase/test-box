import sys

PYTHON = sys.executable,
MODULE = '-m'
TEST = 'py.test',
COVER = 'coverage',

ERASE = COVER + ('erase',)
RUN_APPEND = COVER + ('run', '-a')
HTML = COVER + ('html',)
