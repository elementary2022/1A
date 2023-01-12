#!/usr/bin/env bash

today="$(date +%Y'W'%W'/'%m'-'%d)"
mkdir -p "${today}"
pushd "${today}"
for x in Lang Math English
do
    mkdir -p "${x}"
    pushd "${x}"
    touch README.md
    popd
done

