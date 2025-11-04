pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 --version
                    pip3 --version
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Robot Framework and dependencies...'
                sh '''
                    pip3 install --user -r requirements.txt
                '''
            }
        }
        
        stage('Run Robot Framework Tests') {
            steps {
                echo 'Running Robot Framework tests...'
                sh '''
                    robot --outputdir results \
                          --xunit results/junit-output.xml \
                          tests/calculator_tests.robot
                '''
            }
        }
    }
    
    post {
        always {
            // Publish Robot Framework results using the Robot Framework plugin
            robot(
                outputPath: 'results',
                outputFileName: 'output.xml',
                reportFileName: 'report.html',
                logFileName: 'log.html',
                passThreshold: 100.0,
                unstableThreshold: 75.0,
                onlyCritical: false,
                otherFiles: '*.png,*.jpg'
            )
            
            // Archive JUnit XML for additional reporting
            junit 'results/junit-output.xml'
            
            // Archive test artifacts
            archiveArtifacts artifacts: 'results/**/*', allowEmptyArchive: true
            
            // Clean workspace after build (optional)
            echo 'Build completed!'
        }
        
        success {
            echo '✅ All tests passed successfully!'
        }
        
        failure {
            echo '❌ Tests failed! Check the Robot Framework report for details.'
        }
        
        unstable {
            echo '⚠️ Tests completed with warnings or some failures.'
        }
    }
}
