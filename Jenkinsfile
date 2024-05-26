pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git 'https://github.com/dalitvernersch/world_of_game.git'
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t world-of-game-app .'
            }
        }

        stage('Run') {
            steps {
                // Run the Docker container
                sh 'docker run -d -p 8777:5000 --name world-of-game-app-container -v $(pwd)/Scores.txt world-of-game-app'
            }
        }

        stage('Test') {
            steps {
                // Run Selenium tests using e2e.py
                sh 'python3 test/e2e.py http://localhost:8777'
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
                sh 'docker stop world-of-game-app-container'
                sh 'docker rm world-of-game-app-container'

                // Tag and push the Docker image to DockerHub
               sh 'docker tag world-of-game-app dalitvernersch/world_of_game:latest'
               sh 'docker push dalitvernersch/world_of_game:latest'

            }
        }
    }
}
