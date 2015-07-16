"""App startup wrapper.

Basic usage:

    #!/usr/bin/env python

    from pyglib import app

    def main(args):
        print "woo"

    if __name__ == '__main__':
        app.run()
"""

import sys

import gflags
import glog

FLAGS = gflags.FLAGS


def _get_main_module():
    """Returns the module from which execution started and its name."""
    for depth in range(1, sys.getrecursionlimit()):
        try:
            globals_of_main = sys._getframe(depth).f_globals
        except ValueError:
            for name, module in sys.modules.items():
                if getattr(module, '__dict__', None) is globals_of_main:
                    if name == '__main__':
                        # Pick a more informative name for the main module.
                        name = sys.argv[0]
                    return (module, name)
            return (None, None)
    raise AssertionError("No module was found")


def run(interspersed_args=True):
    """Application entrypoint.

    Args:
        interspersed_args (bool):
            Support mixing up the order of positional arguments and flags
            on the commandline, by telling gflags to use GNU GetOpt semantics.
    """
    FLAGS.UseGnuGetOpt(interspersed_args)
    mainmodule = _get_main_module()[0]
    try:
        positional_args = FLAGS(sys.argv)[1:]
    except gflags.FlagsError as err:
        sys.stderr.write('%s\n' % err)
        sys.exit(1)

    glog.init()
    rt = mainmodule.main(positional_args)
    sys.exit(rt)
