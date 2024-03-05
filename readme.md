# This file describes the steps to run application

## Install mongodb in docker container
    docker-compose up

## Install all project dependencies
    pip install -r requirements.txt

## Create database and import all data into Mongodb
    python setup_database.py

## Run application on localhost
    uvicorn api_endpoints:app --reload  

## Test application on 
    http://127.0.0.1:8000/profile/0D43N0-E


    