#!/usr/bin/env bash

current_dir="$( cd "$( dirname "$0"  )" && pwd  )"
python $current_dir/xcpretty_fix.py | xcpretty