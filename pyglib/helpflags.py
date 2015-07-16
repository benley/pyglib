"""Workarounds for some minor gflags quirks.

If https://github.com/google/python-gflags/pull/18 ever gets merged,
these can go away.
"""
# Copyright (c) 2006, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
