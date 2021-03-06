#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Ruby plugin class."""

from SublimeLinter.lint import RubyLinter


class Ruby(RubyLinter):

    """Provides an interface to ruby -wc."""

    syntax = ('ruby', 'ruby on rails', 'rspec', 'html (rails)')
    cmd = 'ruby -wc'
    regex = (
        r'^.+?:(?P<line>\d+): (?:(?P<error>.*?error)|(?P<warning>warning))[,:] (?P<message>[^\r\n]+)\r?\n'
        r'(?:^[^\r\n]+\r?\n^(?P<col>.*?)\^)?'
    )
    multiline = True
    selectors = {'html (rails)': 'source.ruby.rails.embedded.html'}
    comment_re = r'\s*#'

    def build_cmd(self, cmd=None):
        script = ". /usr/local/share/chruby/chruby.sh; . /usr/local/share/chruby/auto.sh; chruby_auto; ruby -wc"
        return('bash', '-c', script)
