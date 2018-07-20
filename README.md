# thriller-diary-api

An online journal where users can pen down their thoughts and feelings. This is the implementation of the Restful API.

# Status
[![Build Status](https://travis-ci.org/james-chege/thriller-diary-api.svg?branch=develop)](https://travis-ci.org/james-chege/thriller-diary-api) 
[![Coverage Status](https://coveralls.io/repos/github/james-chege/thriller-diary-api/badge.svg?branch=develop)](https://coveralls.io/github/james-chege/thriller-diary-api?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/dcd92dcc85e867b53119/maintainability)](https://codeclimate.com/github/james-chege/thriller-diary-api/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bc05f653d4b3470b84a41ca252d68cbd)](https://www.codacy.com/app/james-chege/thriller-diary?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=james-chege/thriller-diary&amp;utm_campaign=Badge_Grade)

__[Live version](https://thriller-diary-api.herokuapp.com/api/v1)__

__[Pivotal Tracker Stories](https://pivotaltracker.com/n/projects/2183778)__

## folder structure
```
~/thriller-dairy-api
  |__ /app   
      |-- __init__.py
      |-- models.py
      |-- entries.py
      |-- views.py
  |__ /instance
      |-- __init__.py
      |-- config.py
  |__ /tests
      |-- __init__.py
      |-- test_entries.py
  |-- .gitignore
  |--.travis.yml
  |--LICENSE
  |--Readme.md
  |--requirements.txt
  |--run.py
```

### Local Installation

Fork this repository to your github account and clone from there(_NB: clone from your github account - after forking_).This will help you to contribute to this project.

[Create a python Virtual environment and Activate it](https://virtualenv.pypa.io/en/stable/).A virtual environment is effective when working on multiple projects. Each project will have its own development enviroment.

__Install Dependencies__(_Note: This should be done in the created virtual environment_)
```py
 pip install -r requirements.txt
```
__Set environment variable__
```py
 export APP_SETTINGS="development"
```

__Start Server__
```py
python run.py
```

[__Use postman app to send request to app.__](https://www.getpostman.com/)
### Endpoints

The following is a list of available endpoints in this application

|EndPoint               | Functionality|
| ------------------------------------ | ------------------------ |
|GET /api/v1/entries                |Fetch all entries|
|GET /api/v1/entries/<int:entryId>/     |Fetch a single entry|
|POST /api/v1/entries               |Create an entry|
|PUT /api/v1/entries/<int:entryId>/ |Modify an entry|
|DELETE /api/v1/entries/<int:entryId>/ |Delete an entry|

# Testing
```
py.test --cov=app
```

### Contributing
Create A Pull request to develop branch

### Authors
* [James Chege](https://www.github.com/james-chege)

### License

This app is licensed under MIT [LICENSE](LICENSE)
