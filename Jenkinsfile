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
		stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
        stage('Update Kube Config'){
            steps {
                withAWS(region:'us-west-2',credentials:'Jenkins User') {
                    sh 'sudo aws eks --region us-west-2 update-kubeconfig --name udacity-project'
                }
            }
        }
		stage('Deploy Updated Image to Cluster'){
            steps {
                sh '''
                    export IMAGE="$registry:$BUILD_NUMBER"
                    sed -ie "s~IMAGE~$IMAGE~g" kubernetes/container.yml
                    sudo kubectl apply -f ./kubernetes
                    '''
            }
        }
	}
}
		