# ads_portal
Small app being a portal with advertisements. 


# Getting started
Open your terminal
```
$ git clone https://github.com/paubur/ads_portal.git   
$ cd ads_portal # Browse into the repo root directory  
$ pip3 install virtualenv # Virtualenv is a tool to create isolated Python environments  
$ virtualenv -p python <desired-path> #Create virtual enviroment  
$ source venv/bin/activate # Launch the environment  
$ pip3 install -r requirements.txt #Install dependiences  
$ python3 manage.py migrate #Migrate models  
$ python3 manage.py createsuperuser #Create Django Admin  
$ python3 manage.py runserver
```


# Tests
To run tests  
Open your terminal  
```
$ cd ads_portal # Browse into the repo root directory
$ pytest
```


# Docker
To run Docker  
Install DockerMachine https://docs.docker.com/machine/install-machine/ #Instructions  
Install Docker Compose https://docs.docker.com/compose/install/ #Instructions  
```
$ docker-compose up --build
```
  
  
# URL
`/admin`  
`/offers`  
`/offers/{id}`  
`/category`  
`category/{id}`


# FRONTEND

To run frontend  
Install Node.js https://nodejs.org/en/  
Open your terminal  
```
$ npm install -g @angular/cli or npm install -g @angular/cli@next #Install Angular CLI
```

# Development server
Open your terminal
```
& cd Angular10Crud
$ ng serve
```
Navigate to `http://localhost:4200/`

Basic frontend is made only for Category model.

In order to run frontend server, first run backend server. 
