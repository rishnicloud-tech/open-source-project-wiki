pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'open-source-project-wiki'
        CONTAINER_NAME = 'wiki-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f %CONTAINER_NAME% 2>nul || exit /b 0'
                bat 'docker run -d -p 8082:80 --name %CONTAINER_NAME% %DOCKER_IMAGE%'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed! Please check the logs.'
        }
    }
}