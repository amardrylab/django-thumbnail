# Image webserver on Google Cloud Platform

This repository can be used for generating an image webserver on django server
### Steps required for making the webserver
## 1) Clone the ansible script on your local machine

git clone https://github.com/amardrylab/ansible_djangoserver3.git

## 2) Change directory and start the ansible-playbook

- cd ansible-djangoserver3
- ansible-playbook instance_create.yml

## 3) SSH to your created machine

ssh www.drylab.in

## 4) Create your virutual environment

virtualenv myproject

## 5) Install git software

- sudo apt-get update
- sudo apt-get install git

## 6) Clone the django scripts

git clone https://github.com/amardrylab/django-thumbnail.git

## 7) Copy the required file in proper location

mv django-thumbnail/* myproject

## 8) Enter in your virtual environment

- source myproject/bin/activate
- cd myproject

## 9) Install the required softwares in the local environment 

- pip install django
- pip install pillow

## 10) Run the following commands for your final launching

- python manage.py migrations
- python manage.py migrate
- sudo service nginx restart
- sudo service uwsgi restart
