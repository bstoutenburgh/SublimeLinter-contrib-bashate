#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ben Stoutenburgh
# Copyright (c) 2015 Ben Stoutenburgh
#
# License: MIT
#

"""This module exports the Bashate plugin class."""

from SublimeLinter.lint import Linter


class Bashate(Linter):
    """Provides an interface to bashate."""

    syntax = 'shell-unix-generic'
    cmd = 'bashate'
    comment_re = r'\s*#'
    regex = (
        r'^\[(?:(?P<error>E)|(?P<warning>W))\] E\d+: '
        r'(?P<message>.+): \'(?P<near>.+)\'\n - '
        r'(?P<file>.+) : L(?P<line>\d+)'
    )
    multiline = True
    defaults = {
        '--ignore=,': '',
        '--warn=,': '',
        '--error=,': ''
    }
    inline_overrides = ('ignore', 'warn', 'error')
    tempfile_suffix = 'sh'
    check_version = False
