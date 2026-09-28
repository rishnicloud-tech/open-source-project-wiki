pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'open-source-project-wiki'
        CONTAINER_NAME = 'wiki-container'
        SERVER_IP = credentials('aws_ec2_ip')
        SSH_CREDENTIALS = credentials('aws_ssh_key')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate') {
            steps {
                sh 'echo "Validating project files..."'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                sh 'chmod +x scripts/build.sh'
                sh './scripts/build.sh'
            }
        }

        stage('Test') {
            steps {
                sh 'chmod +x scripts/test.sh'
                sh './scripts/test.sh'
            }
        }

        stage('Package (Docker Build)') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Deploy to Cloud (AWS EC2)') {
            steps {
                script {
                    // This is an example of deployment via SSH
                    // In a real environment, you'd use ssh-agent
                    echo "Deploying to AWS EC2: ${SERVER_IP}"
                    
                    /* Example SSH deployment command:
                    sshagent(['aws_ssh_key']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@${SERVER_IP} '
                            docker pull ${DOCKER_IMAGE}
                            docker stop ${CONTAINER_NAME} || true
                            docker rm ${CONTAINER_NAME} || true
                            docker run -d -p 80:80 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}
                        '
                        """
                    }
                    */
                }
            }
        }
        
        stage('Health Check') {
            steps {
                script {
                    echo "Performing health check..."
                    // sh "curl -f http://${SERVER_IP} || exit 1"
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed! Please check the logs."
        }
    }
}
