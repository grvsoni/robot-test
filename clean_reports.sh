#!/bin/bash
# Script to clean up Robot Framework test reports

echo "Cleaning up test reports..."

# Remove results directory
if [ -d "results" ]; then
    rm -rf results/
    echo "✓ Removed results/ directory"
fi

# Remove root-level report files
rm -f output.xml log.html report.html junit-output.xml

echo "✓ Removed root-level reports"
echo "All test reports cleaned successfully!"
