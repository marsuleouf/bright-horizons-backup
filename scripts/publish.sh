#!/bin/bash

# Script to build and publish the package to PyPI using uv

set -e

echo "🔧 Building package..."

# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
uv build

echo "📦 Package built successfully!"

# Check the package
echo "🔍 Checking package..."
uv run twine check dist/*

echo "✅ Package check passed!"

# Upload to PyPI
echo "🚀 Publishing to PyPI..."
uv publish

echo "🎉 Package published successfully!"
echo "Install with: pip install bright-horizons-backup"