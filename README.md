# Python-Project 


## Python Virtual Environment 

[Python Docs](https://docs.python.org/3/library/venv.html)

Create a venv 
`$ python3 -m venv venv`

Activate a venv 
`$ source venv/bin/activate`

Install packages within the venv
`$ python -m pip install <package-name>`

Install packages from requirements.txt
`$ pip install -r requirements.txt`

Specifying requirements in `requirements.txt`
`$ pip freeze > requirements.txt`

Deactivate the venv 
`$ deactivate`


## Mongo DB 

(MongoDB - Docker Docs](https://www.mongodb.com/compatibility/docker)

```sh
# Set the MongoDB version 
export MONGODB_VERSION=6.0-ubi8

# Run a Docker container with the specified MongoDb version, on an accessible local port 
# Update the user and pass variables
docker run --name mongodb -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=pass mongodb/mongodb-community-server:$MONGODB_VERSION

# Stop and Remove the Docker Container, Discard all contents
docker stop mongodb && docker rm mongodb
```

Testing 
(Article)[https://www.mongodb.com/developer/products/mongodb/pytest-fixtures-and-pypi/]

## Pytest  

`pytest` - Run all tests
`pytest -s` - Run all tests, printstdout