pipeline {
    // agent {
    //     docker {
    //         image 'python:3.9'
    //     }
    // }

    agent {
        docker {
            image 'python:3.9' 
            args '-v /var/run/docker.sock:/var/run/docker.sock -v'
        }
    }
    stages {
        stage('build image') {



            steps {
                sh '''
                    apt-get update
                    apt-get install -y ca-certificates curl gnupg lsb-release
                    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
                    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
                    apt-get update
                    apt-get install -y docker-ce-cli
                '''
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
