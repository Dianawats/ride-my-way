
[![Build Status](https://travis-ci.org/Dianawats/ride-my-way.svg?branch=Apiv1)](https://travis-ci.org/Dianawats/ride-my-way) 

[![Maintainability](https://api.codeclimate.com/v1/badges/809627c07a98c069d4b2/maintainability)](https://codeclimate.com/github/Dianawats/ride-my-way/maintainability)

[![Coverage Status](https://coveralls.io/repos/github/Dianawats/ride-my-way/badge.svg?branch=master)](https://coveralls.io/github/Dianawats/ride-my-way?branch=master)

Ride-my-way

is a carpooling application that provides derivers with the ability to create ride offers and passengers to join available ride offers.

Project features:

Get all ride offers
Get a specific ride offer
Create a ride offer
Make a request to join a ride.

Technologies used to develop this app:

Python Language
Flask framework
Postman
Visualcode
Html, CSS and Javascript

To run the unitests:

Pytests
coverage $ nosetests --with-coverage --cover-erase --cover-package=app/ && coverage report

To run the Application:

$ python app.py

Get all project dependencies by running the command below.

$ pip freeze -r requirements.txt

Get started:

clone the repo $ git clone https://github.com/Dianawats/ride-my-way
$ cd into the project directory
set up a virtual environment $ virtualenv venv
Activate the virtual environment
Install project dependencies $ pip install -r requirements.txt
Postman to navigate the API endpoints  http://127.0.0.1:5000/api/v1/ride/1







