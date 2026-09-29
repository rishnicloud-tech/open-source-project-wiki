pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'open-source-project-wiki'
        CONTAINER_NAME = 'wiki-container'
        DOCKER_EXE = 'C:\\Users\\rishn\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat '"%DOCKER_EXE%" build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                "%DOCKER_EXE%" stop %CONTAINER_NAME% 2>nul
                "%DOCKER_EXE%" rm %CONTAINER_NAME% 2>nul
                "%DOCKER_EXE%" stop open-source-project-wiki 2>nul
                "%DOCKER_EXE%" rm open-source-project-wiki 2>nul
                "%DOCKER_EXE%" run -d -p 8080:80 --name %CONTAINER_NAME% %DOCKER_IMAGE%
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