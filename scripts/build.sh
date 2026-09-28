#!/bin/bash
# scripts/build.sh

echo "Starting build process..."

# Create dist directory
mkdir -p dist

# Copy HTML files
cp index.html dist/
cp -r pages dist/

# Copy assets
cp -r css dist/
cp -r js dist/

# Verify copy
if [ -d "dist/pages" ] && [ -d "dist/css" ]; then
    echo "Build successful!"
    exit 0
else
    echo "Build failed! Required files missing."
    exit 1
fi
