pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git 'https://github.com/your/repository.git'
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t my-flask-app .'
            }
        }

        stage('Run') {
            steps {
                // Run the Docker container
                sh 'docker run -d -p 8777:5000 --name my-flask-container -v $(pwd)/dummy_Scores.txt:/Scores.txt my-flask-app'
            }
        }

        stage('Test') {
            steps {
                // Run Selenium tests using e2e.py
                sh 'python e2e.py http://localhost:8777'
            }
            post {
                // Fail the pipeline if tests fail
                failure {
                    echo 'Tests failed!'
                    // You can add more actions here if needed
                }
            }
        }

        stage('Finalize') {
            steps {
                // Terminate the Docker container
                sh 'docker stop my-flask-container'
                sh 'docker rm my-flask-container'

                // Tag and push the Docker image to DockerHub
                sh 'docker tag my-flask-app username/repository:tag'
                sh 'docker push username/repository:tag'
            }
        }
    }
}
