"""Workarounds for some minor gflags quirks.

If https://github.com/google/python-gflags/pull/18 ever gets merged,
these can go away.
"""
import sys

import gflags

FLAGS = gflags.FLAGS


class HelpFlag(gflags.BooleanFlag):
    """Default handler for --help

    HelpFlag is a special boolean flag that prints usage information and raises
    a SystemExit exception if it is ever found in the command line arguments.
    Note this is called with allow_override=1, so other apps can define their
    own --help flag, replacing this one, if they want.
    """

    def __init__(self):
        gflags.BooleanFlag.__init__(self, "help", 0, "show this help",
                                    short_name="?", allow_override=1)

    def Parse(self, arg):
        if arg:
            doc = sys.modules["__main__"].__doc__.replace('%s', sys.argv[0])
            flags = str(FLAGS)
            print doc or ("\nUSAGE: %s [flags]\n" % sys.argv[0])
            if flags:
                print "flags:"
                print flags
            sys.exit(1)


class HelpshortFlag(gflags.BooleanFlag):
    """Default handler for --helpshort

    HelpshortFlag is a special boolean flag that prints usage information for
    the "main" module, and rasies a SystemExit exception if it is ever found in
    the command line arguments.  Note this is called with allow_override=1, so
    other apps can define their own --helpshort flag, replacing this one, if
    they want.
    """

    def __init__(self):
        gflags.BooleanFlag.__init__(self, "helpshort", 0,
                                    "show usage only for this module",
                                    allow_override=1)

    def Parse(self, arg):
        if arg:
            doc = sys.modules["__main__"].__doc__.replace('%s', sys.argv[0])
            flags = FLAGS.MainModuleHelp()
            print doc or ("\nUSAGE: %s [flags]\n" % sys.argv[0])
            if flags:
                print "flags:"
                print flags
            sys.exit(1)
