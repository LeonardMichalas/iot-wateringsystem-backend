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

#Setup MQTT Broker
1. docker pull eclipse-mosquitto
2. docker run -d -p 1883:1883 -p 9001:9001 --name mymqttbroker eclipse-mosquitto
3. docker exec -it mymqttbroker /bin/sh
4. cd mosquitto/config/
5. vi mosquitto.conf
6. allow_anonymous false
7. password_file /etc/mosquitto/passwd
8. cd /etc/
9. mkdir mosquitto
10. touch passwd
11. mosquitto_passwd -b /etc/mosquitto/passwd cougar iot-bootcamp-2019
12. mosquitto_passwd -b /etc/mosquitto/passwd jaguar iot-bootcamp-2019
13. mosquitto_passwd -b /etc/mosquitto/passwd panther iot-bootcamp-2019
14. mosquitto_passwd -b /etc/mosquitto/passwd leopard iot-bootcamp-2019
15. mosquitto_passwd -b /etc/mosquitto/passwd lion iot-bootcamp-2019
16. mosquitto_passwd -b /etc/mosquitto/passwd tiger iot-bootcamp-2019
17. exit
17. docker commit 59cdfe17f429 lmichalas/mqttbroker-iot-bootcamp:0.2
18. docker push lmichalas/mqttbroker-iot-bootcamp:0.2
19. kubectl run mymqttbroker --image=lmichalas/mqttbroker-iot-bootcamp:0.2 --port 1883
20. kubectl expose deployment mymqttbroker --type=LoadBalancer --port 1883 --target-port 1883

#Node red implementation

1. Manage palette -> install -> node-red-dashboard
2. Dashboard appears on IP:Port/ui
3. Network -> MQTT in node -> configure -> new server -> IP und Port -> Security -> Username & Password -> topic definieren (topic has the following pattern: /iot-bootcamp-2019/[groupname]/devices/[CPU SN]/sensors/humidity)
4. Define logic

Cloud -> Edge Device
/iot-bootcamp-2019/[groupname]/devices/[CPU SN]/config/hAct -> hAct (0-100)
/iot-bootcamp-2019/[groupname]/devices/[CPU SN]/config/hMin -> hMin (0-100)
/iot-bootcamp-2019/[groupname]/devices/[CPU SN]/config/hMin -> hMax (0-100)
/iot-bootcamp-2019/[groupname]/devices/[CPU SN]/config/tpumping -> tpumping (0-100s)
/iot-bootcamp-2019/[groupname]/devices/[CPU SN]/config/lrefill -> refill (0-100%)

Edge Device -> Cloud
iot-bootcamp-2019/[groupname]/devices/[CPU SN]/sensors/humidity (0-100)
iot-bootcamp-2019/[groupname]/devices/[CPU SN]/sensors/level (0-100)
iot-bootcamp-2019/[groupname]/devices/[CPU SN]/sensors/button (0,1)
iot-bootcamp-2019/[groupname]/devices/[CPU SN]/actuator/led (0,1)
iot-bootcamp-2019/[groupname]/devices/[CPU SN]/actuator/pump (0,1)
