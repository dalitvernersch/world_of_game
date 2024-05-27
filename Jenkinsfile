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
                sh 'docker run -d -p 8777:5000 --name world-of-game-app-container -v $(pwd)/Scores.txt:/Scores.txt world-of-game-app'
            }
        }

        stage('Test') {
            steps {
                // Run Selenium tests using e2e.py inside the Docker container
                sh 'docker exec world-of-game-app-container python3 /app/test/e2e.py http://localhost:8777'
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

               withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
    // Login to Docker Hub
    sh "echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin"
    // Tag and push the Docker image to the new DockerHub repository
    sh 'docker tag world-of-game-app $DOCKER_HUB_USERNAME/world_of_game:latest'
    sh 'docker push $DOCKER_HUB_USERNAME/world_of_game:latest'
}

            }
        }
    }
}
