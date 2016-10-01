pyglib: Simplified scripting with gflags and glog
=================================================

pyglib provides a clean, consistent setup for writing commandline
scripts and applications in Python. It makes use of python-gflags and
python-glog, and adds an app startup helper that deals with
initialization boilerplate so you don't have to think about it.

**NOTE:** you may also want to check out google.apputils.app_, (part of
google-apputils_) which does something extremely similar to this module.  If I
had been aware of that project's existence in summer 2015, I probably would not
have created this one.  This module is considerably simpler and smaller in
scope than google-apputils, so perhaps you'll still find it useful.

Example usage:
--------------

.. code:: python

    #!/usr/bin/env python

    from pyglib import app, gflags, log

    gflags.DEFINE_integer('bananas', 7, 'Number of bananas.')

    FLAGS = gflags.FLAGS


    def main(args):
        log.info('There are %s bananas.', FLAGS.bananas)
        log.debug('This will only show up if you run with --verbosity=10')


    if __name__ == __main__:
        app.run()

The above module is usable as a commandline app, complete with argument
parsing and validation. It automatically has a few flags like ``--help``
and ``--verbosity`` that come from gflags and glog. Any positional
arguments left over after parsing flags are passed along to the main()
function.

This example module can also be imported as a library for use in another
app. When used that way, any script that imports this one will inherit
the ``--bananas`` flag defined here.

.. _google.apputils.app: https://github.com/google/google-apputils/blob/master/google/apputils/app.py
.. _google-apputils: https://github.com/google/google-apputils
