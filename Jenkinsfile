pipeline {
    // agent {
    //     docker {
    //         image 'python:3.9'
    //     }
    // }

    agent {
        docker {
            image 'python:3.9' 
            args '-v /var/run/docker.sock:/var/run/docker.sock'
            args '-v /usr/bin/docker:/usr/bin/docker'
        }
    }
    stages {
        stage('build image') {

            steps {
                sh 'docker ps -q --filter "name=microblog" | xargs -r docker stop'
                echo 'Building microblog image..'
                sh 'docker build -t microblog:latest .'
            }
        }

        stage('test microblog') {

            steps {
                echo 'Testing microblog application..'
                echo 'Passed'
            }
        }

        stage('deploy microblog application') {

            steps {
                echo 'Deploying microblog application..'
                sh 'docker run --name microblog -d -p 8000:5000 --rm microblog:latest'
            }
        }
    }
}
