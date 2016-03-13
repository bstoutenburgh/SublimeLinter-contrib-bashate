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
import os


class Bashate(Linter):
    """Provides an interface to bashate."""

    syntax = 'shell-unix-generic'
    cmd = 'bashate'
    comment_re = r'\s*#'
    regex = (
        r'^\[(?:(?P<error>E)|(?P<warning>W))\] E\d+: '
        r'(?P<message>.+): \'(?P<near>.+)\'\n - '
        r'.+ : L(?P<line>\d+)'
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

    def tmpfile(self, cmd, code, suffix=''):
        """
        Run an external executable using a temp file to pass code and return its output.

        We override this to have the tmpfile extension match what is being
        linted so E005 is valid.
        """

        filename, extension = os.path.splitext(self.filename)
        extension = '.missingextension' if not extension else extension
        return super().tmpfile(cmd, code, extension)
