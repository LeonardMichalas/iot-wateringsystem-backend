# iot-wateringsystem-backend

# Setup Kubernetes cluster on Google Cloud Platform (GCP)

1. Create new project [projectname]
2. Enable Kubernetes engine API for the project
3. gcloud config set project [projectname]
4. gccloud config set compute/zone europe-west1-b
5. gcloud container clusters create gd-cluster --num-nodes=3
6. gccloud compute instances list

# Deployment of the Service

1. docker pull lmichalas/iot-wateringsystem-backend
2. kubectl run iot-wateringsystem-backend --image=lmichalas/iot-wateringsystem-backend --port 8080
3. kubectl get pods
4. kubectl expose deployment iot-wateringsystem-backend --type=LoadBalancer --port 80 --target-port 8080
5. kubectl get services -> Get IP Adress!(this may take some minutes)
6. kubectl scale deployment iot-wateringsystem-backend --replicas=2
7. kubectl get pods

#Modify Node red image

1. docker run -d -p 1880:1880 --name mynodered nodered/node-red
2. docker exec -it mynodered /bin/bash
3. cd /usr/src/node-red/node_modules/node-red
4. node -e "console.log(require('bcryptjs').hashSync(process.argv[1], 8));" iot-bootcamp-2019
$2a$08$Pa6duKiNyQ2Lo/khA/D/5Ob0/OOlhG4lyl3ag8ZFeoZpuzR2VHFz.
5. Copy hash
6. vi settings.js
7. Uncomment "AdminAuth" Section
8. replace the password with the generated hash
9. exit
10. docker commit c8c3020f4b2a lmichalas/node-red-iot-bootcamp:0.1
11. docker push lmichalas/node-red-iot-bootcamp:0.1

# Setup Node red
1. docker pull nodered/node-red
2. kubectl run node-red --image=nodered/node-red --port 1880
3. kubectl expose deployment node-red --type=LoadBalancer --port 80 --target-port 1880
