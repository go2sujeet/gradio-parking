#!/bin/bash
# Assumes a VERSION file with the version e.g., 1.0.0
VERSION=$(cat VERSION)
NEW_VERSION=$(npx semver $VERSION -i patch)
echo $NEW_VERSION > VERSION
git add VERSION
git commit -m "Increment version to $NEW_VERSION"
