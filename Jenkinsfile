pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'open-source-project-wiki'
        CONTAINER_NAME = 'wiki-container'
        DOCKER = 'C:\\Users\\rishn\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat '"%DOCKER%" build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                "%DOCKER%" stop %CONTAINER_NAME% 2>NUL || exit /b 0
                "%DOCKER%" rm %CONTAINER_NAME% 2>NUL || exit /b 0
                "%DOCKER%" run -d -p 8082:80 --name %CONTAINER_NAME% %DOCKER_IMAGE%
                '''
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