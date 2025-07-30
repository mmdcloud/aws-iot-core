#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-dev
sudo apt-get install -y python3-venv
sudo apt-get install -y awscli
sudo apt-get install -y jq
python3 -m pip install awsiotsdk