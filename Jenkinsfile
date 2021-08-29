
pipeline {
    environment {
        name = 'Om Prakash'
    }

   agent {
       any
   }

   parameters{
   string(defaultValue: "None", description: 'Enter your name:', name: 'name')
   }

stages{
    stage('Update '){
        steps {
            sh'''
            echo "welcome"
            '''
        }
    }
   }
  }