# Sample Python App Kubernetes Deployment + Monitoring

This repository contains: a sample Python app, Dockerfile, Kubernetes manifests (Deployment, Service, Ingress, HPA) and monitoring integration with Prometheus & Grafana . 

## Prerequisites
- A Kubernetes cluster (minikube)
- kubectl configured to talk to the cluster
- (Optional) Helm 3 installed
- An ingress controller 
- Docker (to build images)

## Steps
---------------
Start the minikube cluster to run the pod with python Docker image
---------------

minikube start --driver=docker --cpus=2 --memory=2200mb
minikube status

docker build -t python-app:latest -f ./python_app/Dockerfile ./python_app
docker images

--------------
Apply manifest files
---------------
kubectl apply -f k8s-manifests/deployment.yaml
kubectl apply -f k8s-manifests/service.yaml
kubectl apply -f k8s-manifests/ingress.yaml
kubectl apply -f k8s-manifests/hpa.yaml

kubectl get pods 

---------
Add & Install kube-prometheus-stack
---------
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
