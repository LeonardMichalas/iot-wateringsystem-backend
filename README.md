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
