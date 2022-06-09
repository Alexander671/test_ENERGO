# test_ENERGO
<p align="center">
<img src="https://img.shields.io/badge/server-drf-red"> 
<img src="https://img.shields.io/badge/mesasge--broker-kafka-black">
<img src="https://img.shields.io/badge/container-docker-blue">
<img src="https://img.shields.io/badge/jwt__auth-rest__framework__simplejwt-blue">

</p>

A simple python backend service that contain two math tasks. 

### First task
A service that will find the roots of the quadratic equation **$a\cdot x^2 + b\cdot x + c = 0$**. The values ​​a, b, c are passed to the service as input.

### Second task
There is a group of 100 items. Items can be blue, green and red. It is known that there are much more blue objects than green ones, and slightly more green objects than red ones. Write a service that will take the number of an item and try to guess its color. 
The service using a simple **formula of probability theory (P=m/n)** will try to understand what color the object is.

### Tested
on Ubuntu 20.04 and is compatable with
```Python==3.8.10
Django==4.0.5
django_environ==0.8.1
djangorestframework==3.13.1
environ==1.0
djangorestframework_simplejwt==5.2.0

```


# CONTENTS:
[Description](#description) </br>
[Deploy](#deploy)           </br>
[Test](#test)               </br>

## Description <a name="description"></a>
**API methods are divided into two types:** 

### Task 1
- **GET/POST/DELETE** methods for the quadratic equation.

### Task 2
- **GET/POST/** method for objects, only for Admin user.
- **GET/POST/** method for attempt to guess what color the object is, only for auth.

**The system has 6 main path:**
-  
+ Standart auth
  + accounts/
    + accounts/login
    + accounts/signup
  
+ Task 1
  +  api/equations/ 

+ Task 2 
  + api/luftballons/
  + api/luftballons/<int:pk>
  + api/luftballons/guess

**Endpoints example:**

*Request:* 
```
GET http://127.0.0.1:8000/api/luftballons/
```
*Response:* 
```
[
    {
        "ball": 0,
        "id": 1,
        "update": 1,
        "guessed": true
    },
    {
        "ball": 0,
        "id": 2,
        "update": 1,
        "guessed": false
    }
    ...
]
    
```

*Request:* 
```
POST http://127.0.0.1:8000/api/equations/

Content type: application/json
{
       "a": 1,
       "b": 4,
       "c": 3
}

```
*Response:* 
```
[
    {
        "id": 1,
        "a": 1,
        "b": 4,
        "c": 3,
        "d": 4.0,
        "x1": -1.0,
        "x2": -3.0
    }
]
```


Some edge-cases examples are available on the [test_postman](https://github.com/Alexander671/test_ENERGO/tree/main/test_postman)
              </br>

## Getting Started <a name="deploy"></a>
These instructions will get you a copy of the project up and running on your local machine. There are **two** ways to run a project.

1. run without Docker
2. run with Docker 

### Build Without Docker

#### Git

Clone the repository
```
git clone https:https://github.com/Alexander671/test_ENERGO/
```

Navigate into the `test_ENERGO` directory
```
cd test_ENERGO/test_ENERGO
```
Create user and password in test_ENERGO app to get Admin user
```
python3 manage.py createsuperuser
```


#### .env file

For correct work you need to create .env file in ~/PROJECT_DIR/test_ENERGO/test_ENERGO/.env
with the following content:

```
nano .env 
```

```
# example
# your django_secret_key
SECRET_KEY="django-insecure-8)+2eujbv7(i0if^h%mmjtxzwz8l1br2^sgcx&w0x*@@uy5@nx"
DEBUG=True
ALLOWED_HOSTS=

```

#### Dependencies

Install, using `pip`:

```
pip install -r requirements.txt
```


#### Usage
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

```

### Build Using Docker

#### Git

Clone the repository
```
git clone https://github.com/Alexander671/test_ENERGO/
```

Navigate into the `test_ENERGO` directory
```
cd test_ENERGO/test_ENERGO
```

Create user and password in test_ENERGO app to get Admin user
```
python3 manage.py createsuperuser
```


#### .env file

For correct work you need to create .env file in ~/PROJECT_DIR/test_ENERGO/test_ENERGO/.env
with the following content:

```
nano .env 
```

```
# example
# your django_secret_key
SECRET_KEY="django-insecure-8)+2eujbv7(i0if^h%mmjtxzwz8l1br2^sgcx&w0x*@@uy5@nx"
DEBUG=True
ALLOWED_HOSTS=

```

#### Usage

1. Build the image

`docker build .`

2. Сompiling the image with the team

`docker-compose build`

3. Run container:

`docker-compose up -d`

## Some examples and test <a name="test"></a>

Some edge-cases examples are available on the [test_postman](https://github.com/Alexander671/test_ENERGO/)

## Authors

* **Alexander Matveev** - *Initial work* - [Alexander671](https://github.com/Alexander671)
