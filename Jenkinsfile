# payment_gateway/Jenkinsfile
pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Lint') {
      steps {
        sh 'flake8 app/'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest tests/'
      }
    }
    stage('Build Docker') {
      steps {
        sh 'docker build -t payment-api .'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker-compose up -d --build'
      }
    }
  }
}