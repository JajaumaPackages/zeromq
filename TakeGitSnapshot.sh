#!/bin/bash

set -e
tempDir=$(mktemp -d)
checkoutDir=$tempDir/zeromq
git clone --quiet https://github.com/zeromq/libzmq "$checkoutDir"
tar -C "$tempDir" -cjf zeromq.tar.bz2 zeromq

lastTag=$(cd "$checkoutDir"; git describe --tags --abbrev=0 | sed 's/^v//')
headCommit=$(cd "$checkoutDir"; git rev-list HEAD -n 1 | cut -c 1-7)

echo "%global gitdate $(date +%Y%m%d)"
echo "%global gitversion ${lastTag}"
echo "%global gitcommit ${headCommit}"

rm -rf "$tempDir"
