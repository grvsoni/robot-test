# Jenkins Pipeline Setup Guide

This guide explains how to set up a Jenkins pipeline for running Robot Framework tests automatically.

## Prerequisites

- ✅ Jenkins installed and running (http://localhost:8080/)
- ✅ Robot Framework Plugin installed in Jenkins
- ✅ Python 3 installed on Jenkins agent
- ✅ Git installed on Jenkins agent

## Jenkins Pipeline Features

The pipeline includes:
- **Automatic checkout** from Git repository
- **Dependency installation** (Robot Framework)
- **Test execution** with Robot Framework
- **Result publishing** using Robot Framework Plugin
- **JUnit XML reporting** for test results
- **Artifact archiving** for reports and logs

## Setup Steps

### 1. Create a New Pipeline Job

1. Open Jenkins at http://localhost:8080/
2. Click **"New Item"**
3. Enter a name: `robot-test-pipeline`
4. Select **"Pipeline"**
5. Click **"OK"**

### 2. Configure Pipeline

In the Pipeline configuration page:

#### General Settings
- ✅ Check **"GitHub project"** (optional)
  - Project url: `https://github.com/grvsoni/robot-test/`

#### Build Triggers (Optional)
Choose one or more:
- ✅ **Poll SCM**: `H/5 * * * *` (checks every 5 minutes)
- ✅ **GitHub hook trigger for GITScm polling** (for webhook integration)

#### Pipeline Definition
1. **Definition**: Select **"Pipeline script from SCM"**
2. **SCM**: Select **"Git"**
3. **Repository URL**: `https://github.com/grvsoni/robot-test.git`
4. **Branch Specifier**: `*/main`
5. **Script Path**: `Jenkinsfile`

Or alternatively, use **"Pipeline script"** and paste the contents of the Jenkinsfile directly.

### 3. Save and Build

1. Click **"Save"**
2. Click **"Build Now"** to run the pipeline

## Pipeline Stages

The pipeline executes the following stages:

### Stage 1: Checkout
- Checks out the code from Git repository

### Stage 2: Setup Python Environment
- Verifies Python and pip are available
- Displays version information

### Stage 3: Install Dependencies
- Installs Robot Framework from requirements.txt

### Stage 4: Run Robot Framework Tests
- Executes all test cases
- Generates HTML reports (report.html, log.html)
- Generates JUnit XML output

### Post-Build Actions
- **Robot Framework Plugin**: Publishes interactive test results
- **JUnit Plugin**: Publishes test results in JUnit format
- **Archive Artifacts**: Saves all test reports and logs

## Viewing Results

After the build completes:

### 1. Robot Framework Report
- Click on the build number
- Click **"Robot Framework Results"** in the left menu
- View interactive test statistics, trends, and detailed logs

### 2. JUnit Test Results
- Click on **"Test Results"** in the left menu
- View test pass/fail statistics and trends

### 3. Archived Artifacts
- Click on **"Build Artifacts"**
- Download `report.html`, `log.html`, or `output.xml`

## Pass/Fail Thresholds

The pipeline is configured with:
- **Pass Threshold**: 100% (all tests must pass)
- **Unstable Threshold**: 75% (build marked unstable if below this)

You can adjust these in the Jenkinsfile:
```groovy
robot(
    passThreshold: 100.0,      // Change this value
    unstableThreshold: 75.0,   // Change this value
    ...
)
```

## Running Tests Locally Before Pushing

Before pushing code to trigger Jenkins:
```bash
# Run tests locally
robot tests/calculator_tests.robot

# Clean up reports
./clean_reports.sh

# Run tests with same output format as Jenkins
robot --outputdir results --xunit results/junit-output.xml tests/calculator_tests.robot
```

## Troubleshooting

### Issue: Python not found
**Solution**: Install Python 3 on Jenkins agent or configure Python path in Jenkins

### Issue: pip install fails
**Solution**: Use `pip3 install --user -r requirements.txt` in Jenkinsfile

### Issue: Robot Framework plugin not showing results
**Solution**: 
1. Verify plugin is installed: Manage Jenkins → Plugins
2. Check the output path matches in Jenkinsfile
3. Ensure `output.xml` is generated in the results directory

### Issue: Tests fail in Jenkins but pass locally
**Solution**: Check workspace permissions and Python/dependency versions

## CI/CD Best Practices

1. **Run tests before committing**: Always test locally first
2. **Keep tests fast**: Optimize test execution time
3. **Fix failures immediately**: Don't let broken tests accumulate
4. **Monitor trends**: Use Jenkins graphs to track test stability
5. **Clean workspace**: Use cleanup scripts to avoid test pollution

## Advanced Configuration

### Email Notifications
Add to the `post` section in Jenkinsfile:
```groovy
post {
    failure {
        mail to: 'your-email@example.com',
             subject: "Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
             body: "Build failed. Check console output at ${env.BUILD_URL}"
    }
}
```

### Parallel Test Execution
Split tests into multiple stages:
```groovy
stage('Run Tests in Parallel') {
    parallel {
        stage('Addition Tests') {
            steps {
                sh 'robot --include addition tests/calculator_tests.robot'
            }
        }
        stage('Other Tests') {
            steps {
                sh 'robot --exclude addition tests/calculator_tests.robot'
            }
        }
    }
}
```

### Scheduled Builds
Run tests automatically:
- Every night: `H 0 * * *`
- Every hour: `H * * * *`
- Weekdays at 9am: `0 9 * * 1-5`

## Additional Resources

- [Robot Framework Plugin Documentation](https://plugins.jenkins.io/robot/)
- [Jenkins Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
