#!/usr/bin/env bash

xcpretty_wrapper="scripts/xcpretty_fix.sh"
chmod +x "${xcpretty_wrapper}"

set -x

cat tests/xcodebuild.log | xcpretty
cat tests/xcodebuild.log | ${xcpretty_wrapper}
