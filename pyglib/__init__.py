"""pyglib: namespace stuff"""

import gflags
import glog

from pyglib import helpflags

gflags.DEFINE_flag(helpflags.HelpFlag())
gflags.DEFINE_flag(helpflags.HelpshortFlag())

del helpflags

flags = gflags
log = glog

__all__ = ['flags', 'gflags', 'log', 'glog']
