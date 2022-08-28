pipeline {
    agent any

    stages {
        stage('Python Test Job') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                step 'python3 --version'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'python3 random.py'
            }
        }
    }
}