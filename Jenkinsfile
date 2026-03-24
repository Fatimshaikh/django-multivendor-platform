pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "django-multivendor"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
            }
        }

        stage('Run Migrations') {
            steps {
                sh 'docker-compose run web python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker-compose run web python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment step — here you can deploy to your server or staging environment'
            }
        }
    }
}