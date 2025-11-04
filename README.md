# Calculator Application with Robot Framework Tests

A simple Python calculator application with comprehensive Robot Framework test coverage.

## Project Structure

```
robot-test/
├── calculator.py              # Main calculator application
├── tests/
│   ├── calculator_tests.robot # Robot Framework test suite (4 test cases)
│   └── CalculatorLibrary.py   # Robot Framework keyword library
├── requirements.txt           # Python dependencies
├── clean_reports.sh           # Script to clean up test reports
├── Jenkinsfile                # Jenkins pipeline configuration
├── JENKINS_SETUP.md           # Detailed Jenkins setup guide
└── README.md                  # This file
```

## Features

The calculator supports four basic arithmetic operations:
- **Addition**: Add two numbers
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero division protection)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

Execute all tests:
```bash
robot tests/calculator_tests.robot
```

Execute tests with JUnit XML output:
```bash
robot --xunit junit-output.xml tests/calculator_tests.robot
```

Run tests with specific tags:
```bash
robot --include addition tests/calculator_tests.robot
robot --include multiplication tests/calculator_tests.robot
```

Generate detailed test report in a specific directory:
```bash
robot --outputdir results tests/calculator_tests.robot
```

Generate both standard and JUnit XML output:
```bash
robot --outputdir results --xunit results/junit-output.xml tests/calculator_tests.robot
```

## Test Cases

The test suite includes 4 comprehensive test cases:

1. **Test Addition** - Validates addition operations with positive, negative, and decimal numbers
2. **Test Subtraction** - Validates subtraction operations including negative results
3. **Test Multiplication** - Validates multiplication with various number types
4. **Test Division** - Validates division operations and proper error handling for division by zero

## Test Results

After running tests, Robot Framework generates the following files:
- `output.xml` - Detailed execution results in Robot Framework XML format
- `log.html` - Detailed test execution log
- `report.html` - High-level test report
- `junit-output.xml` - JUnit XML format output (when using --xunit flag)

Open `report.html` in your browser to view a summary of test results.

The JUnit XML output is compatible with CI/CD systems like Jenkins, GitLab CI, GitHub Actions, and other tools that support JUnit XML test reports.

## Cleaning Up Test Reports

Robot Framework overwrites reports when running tests to the same location. However, to manually clean up old reports:

**Using the cleanup script:**
```bash
./clean_reports.sh
```

**Manual cleanup:**
```bash
# Remove all reports
rm -rf results/
rm -f output.xml log.html report.html junit-output.xml
```

## Jenkins CI/CD Integration

This project includes a Jenkins pipeline for automated testing. The pipeline:
- ✅ Automatically checks out code from Git
- ✅ Installs dependencies (Robot Framework)
- ✅ Runs all test cases
- ✅ Publishes Robot Framework test results with interactive reports
- ✅ Generates JUnit XML output for additional reporting
- ✅ Archives test artifacts (logs, reports)

### Quick Setup

1. **Ensure Jenkins has the Robot Framework Plugin installed**
   - Navigate to: Manage Jenkins → Plugins
   - Install: "Robot Framework Plugin"

2. **Create a Pipeline Job**
   - Click "New Item" → Enter name → Select "Pipeline"
   - Under Pipeline section:
     - Definition: "Pipeline script from SCM"
     - SCM: "Git"
     - Repository URL: `https://github.com/grvsoni/robot-test.git`
     - Script Path: `Jenkinsfile`

3. **Run the Pipeline**
   - Click "Build Now"
   - View results in "Robot Framework Results"

### Detailed Instructions

For complete Jenkins setup instructions, troubleshooting, and advanced configuration, see **[JENKINS_SETUP.md](JENKINS_SETUP.md)**.

### Pipeline Stages

1. **Checkout** - Clone repository
2. **Setup Python Environment** - Verify Python/pip
3. **Install Dependencies** - Install Robot Framework
4. **Run Tests** - Execute all test cases
5. **Publish Results** - Generate reports and publish to Jenkins
