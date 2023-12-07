#!/bin/sh

# Set the colorscheme using wal
wal "$@"

# Restart qtile (assuming qtile's command-line client `qtile-cmd` is available)
qtile cmd-obj -o cmd -f reload_config

