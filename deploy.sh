#!/usr/bin/env sh
mkdocs build
mkdocs gh-deploy
# git add -f site && git commit -m "Deploy to Github Pages"
