pipeline {
    agent any

    environment {
        SNOWFLAKE_USER = 'mrajamani' // Jenkins credentials
        SNOWFLAKE_PASSWORD ='Muruga@20608'
        SNOWFLAKE_ACCOUNT = 'POC_ITIM'
        SNOWFLAKE_DATABASE = 'POC_CICD_PY'
        SNOWFLAKE_WAREHOUSE = 'POC_ITIM_PERIASAMY'
        //EMAIL_RECIPIENTS = 'manjunathbabur88@gmail.com'
    }

    parameters {
        booleanParam(name: 'RUN_SQL', defaultValue: true, description: 'Run SQL Module')
        booleanParam(name: 'RUN_PYTHON', defaultValue: true, description: 'Run Python Module')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/manjunathbabur/POC_PROJECT.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run SQL Module') {
            when {
                expression { return params.RUN_SQL }
            }
            steps {
                script {
                    sh '''
                    for file in $(ls sql/*.sql); do
                        echo "Executing SQL file: $file"
                        venv/bin/python python/main.py --sql_file=$file
                    done
                    '''
                }
            }
        }

        stage('Run Python Module') {
            when {
                expression { return params.RUN_PYTHON }
            }
            steps {
                script {
                    sh '''
                    venv/bin/python python/main.py
                    venv/bin/python -m unittest discover python/tests/
                    '''
                }
            }
        }
    }

   
}
