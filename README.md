SublimeLinter-contrib-bashate
================================

[![Build Status](https://travis-ci.org/maristgeek/SublimeLinter-contrib-bashate.svg?branch=master)](https://travis-ci.org/maristgeek/SublimeLinter-contrib-bashate)

This linter plugin for SublimeLinter provides an interface to [bashate](https://pypi.python.org/pypi/bashate). It will be used with files that have the “Shell-Unix-Generic” syntax (aka Shell Script (Bash)).

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `bashate` is installed on your system. To install `bashate`, do the following:

1. For best performance, install [Python 3](http://python.org) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `bashate` by typing the following in a terminal, replacing '3.x' with the available version of pip:
   ```
   [sudo] pip-3.x install bashate
   ```

In order for `bashate` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter.  The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-contrib-bashate settings:

|Setting|Description|
|:------|:----------|
|ignore|A comma-separated list of rules to ignore|
|warn|A comma-separated list of rules to always warn (rather than error)|
|error|A comma-separated list of rules to always error (rather than warn)|
