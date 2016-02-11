import subprocess
import sys


class Runner(object):
    pass


class Python(Runner):
    pass


class Module(object):

    name = None
    python = sys.executable,
    module = '-m',

    @classmethod
    def _run(cls, args):
        my_args = cls.python + cls.module + cls.name + cls.args
        subprocess.call(my_args)



