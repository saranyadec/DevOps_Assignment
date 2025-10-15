#!/bin/bash
kubectl rollout undo deployment/nodejs-app
kubectl get all
