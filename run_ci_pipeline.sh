#!/bin/bash
echo "Starting Professional QA Pipeline..."
pytest test_integration.py --html=report.html --self-contained-html
echo "Pipeline finished successfully!"
