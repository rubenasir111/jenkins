pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "${WORKSPACE}/venv"
        PATH = "${VIRTUAL_ENV}/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Crear entorno virtual') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=test-results/results.xml
                '''
            }
        }

        stage('Publicar resultados') {
            steps {
                junit '**/test-results/*.xml'
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t jenkins:v1 .'
            }
        }

        stage('Desplegar en Kubernetes') {
            steps {
                sh '''
                    minikube start --driver=docker || true
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
