# iot-wateringsystem-backend

#Setup Kubernetes cluster on Google Cloud Platform (GCP)

1. Create new project [projectname]
2. Enable Kubernetes engine API for the project
3. gcloud config set project [projectname]
4. gccloud config set compute/zone europe-west1-b
5. gcloud container clusters create gd-cluster --num-nodes=3
6. gccloud compute instances list
