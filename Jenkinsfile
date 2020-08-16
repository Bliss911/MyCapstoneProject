pipeline {
environment {
    registry = "innociousbliss/capstonehello"
    registryCredential = 'DockerHubCred'
    dockerImage = ''
}
	agent any
	stages {
		stage('Linting') {
			steps {
				sh 'tidy -q -e *.html'
			}
		}
		stage('Cloning our Git') {
			steps {
				git 'https://github.com/Bliss911/MyCapstoneProject.git'
			}
		}
		stage('Building our image') {
			steps{
				script {
					dockerImage = docker.build registry + ":$BUILD_NUMBER"
				}
			}
		}
		stage('Deploy our image') {
			steps{
				script {
					docker.withRegistry( '', registryCredential ) {
						dockerImage.push()
					}
				}
			}
		}
	}
}
		