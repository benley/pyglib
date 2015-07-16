pyglib: Simplified scripting with gflags and glog
=================================================

pyglib provides a clean, consistent setup for writing commandline
scripts and applications in Python. It makes use of python-gflags and
python-glog, and adds an app startup helper that deals with
initialization boilerplate so you don't have to think about it.

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
