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
                junit 'test-results/*.xml'
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t jenkins:v1 .'
            }
        }

        stage('Preparar Minikube') {
            steps {
                sh '''
                    echo "Otorgando permisos al directorio .minikube"
                    sudo chown -R $USER $HOME/.minikube || true
                    sudo chmod -R u+wrx $HOME/.minikube || true

                    echo "Iniciando Minikube con driver Docker"
                    minikube start --driver=docker || true
                '''
            }
        }

        stage('Desplegar en Kubernetes') {
            steps {
                sh '''
                    echo "Aplicando deployment y service en Kubernetes"
                    kubectl apply -f k8s/deployment.yaml || exit 1
                    kubectl apply -f k8s/service.yaml || exit 1
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
