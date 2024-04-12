#!/bin/bash

# Change to the specified directory
# cd ~/simplon/briefs/b15_ajax/github/

# Authenticate to the Azure Container Registry
docker login lpb15ajax.azurecr.io -u lpb15ajax -p "7zzSc1eXxfMte4tvsza6oD2pmUgTFVdymFt6BzTlSk+ACRCtzB4S"

# Build and push the b15back image
docker build -t b15back -f Dockerfile.back .
docker tag b15back lpb15ajax.azurecr.io/back:8000
docker push lpb15ajax.azurecr.io/back:8000

# Wait for integration of FQDN
# Insert the FQDN manually in the instance created
echo "Please integrate the FQDN in the instance created. 
When you get the domainename of your instance b15back, 
you can copy paste it in the port of your script.js file of your front repository and replace in line 8.
Waiting for 6 minutes..."
sleep 360

# Build and push the b15front image
docker build -t b15front -f Dockerfile.front .
docker tag b15front lpb15ajax.azurecr.io/front:3008
docker push lpb15ajax.azurecr.io/front:3008


