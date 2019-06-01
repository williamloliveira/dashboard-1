pipeline {

    agent any;

    stages {

        stage('preparacao') {


            steps {
                echo "Preparando a máquina..."

                git

                sh "docker "

                sleep 10; 
            }

        }

        stage('build') {
            echo "Buildando a aplicação..."
            sleep 10;

        }

        stage('result') {
            steps {
                echo 'Aplicação deployada com sucesso!'
            }
        }

    }
}