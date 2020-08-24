# Capstone Project
#### A Rolling Deployment for a simple Flask app

The flask app runs on
http://ae3fa5c69e5f011eabdb90a1b8238fdf-801216271.us-west-2.elb.amazonaws.com/

### How I achieved this project
1. Provisioned an Amazon EC2 Ubuntu 18.04 Instance.
2. Installed the following softwares
    - Jenkins
    - Docker
    - Hadolint
    - Make
    - Pylint
    - AWS CLI
    - kubectl
    - eksctl
3. Created IAM user with Admin priviledges
4. Configured and logged in to Jenkins
5. Added AWS and DockerHub credentials in Jenkins and installed the following plugins
    * Blue Ocean
    * aws-code-pipeline plugin
6. Created a Elastic Kubernetes cluster
7. Created my Project on GitHub, created and added a key to my repo, then cloned it to my local.
8. Finally deployed complete project to Github.

## Thanks for the opportunity to learn and acquire a great ondemand skill


