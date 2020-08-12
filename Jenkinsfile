pipeline {
environment {
    dockerImage = ''
}
	agent any
	stages {
		stage('Dockerfile linting') {
		    steps {
		        sh 'make lint'
            }
		}
	}
}
