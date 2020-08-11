pipeline {
environment {
    dockerImage = ''
}
	agent any
	stages {
		stage('Linting') {
			steps {
				sh 'tidy -q -e *.html'
			}
		}
		stage('Dockerfile linting') {
		    steps {
		        sh 'make lint'
            }
		}
	}
}
