node ("aws_slave") {

	if (!env.CHANGE_ID) {
    echo "Skipping branch build for ${env.BRANCH_NAME}"
    currentBuild.result = 'SUCCESS'
    return
  }



stage("Code Analysis"){
build job: "chatbot/sonar_checker"
}
// Now to do rest of functionalites

stage("Tests"){
	checkout scm
try{

sh '''
sudo apt-get update

python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
python3 test_app.py
'''
currentBuild.result="SUCCESS"


}catch(err){
currentBuild.result="FAILURE"
error("Test failes: ${err}")
}


}

// Now for approval as to merge the PR 
    stage("Approval") {
        script {
            if (env.CHANGE_ID && (currentBuild.result == "SUCCESS" || currentBuild.result == null)) {
                input message: "OG on the way, wanna merge?", ok: "Merge"
            }
	sh'sleep 12'
        }
    }

stage("Done") {
        script {
            if (currentBuild.result == "SUCCESS" || currentBuild.result == null) {
				
				

               
                sh '''
				
                echo "Everything is working great!"
                '''

			
            } else {
                echo "Build failed — Better luck next time"
            }
        }
    }

}
