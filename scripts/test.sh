#!/bin/bash
# scripts/test.sh

echo "Starting tests..."

# Check if build directory exists
if [ ! -d "dist" ]; then
    echo "Test Failed: dist directory not found. Run build first."
    exit 1
fi

# Check essential files
FILES=("dist/index.html" "dist/css/style.css" "dist/js/script.js" "dist/pages/cloud-computing.html")

for file in "${FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "Test Failed: $file is missing."
        exit 1
    fi
done

echo "All tests passed successfully!"
exit 0
