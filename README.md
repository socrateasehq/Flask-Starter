# [Flask-Starter](#)

**Flask-starter** contains some boilerplate Flask and SQLAlchemy code to help you quickly set up a new Flask project.

## Installation
Install Python 3.8.10 and the latest version of PostgreSQL
git clone https://github.com/Kalebu/Flask-starter

## Create and enter a virtual environment
```bash
cd Flask-starter
python3 -m venv virtualenv
source virtualenv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
pip install setuptools --upgrade
pip install -r requirements.txt
```

## How to run

```bash
python app.py
```


## Migrating database 
Once you modified the models codebase to mirror the change to the database without deleting it, use *flask migrate*, but before we do that we need to tell flask where entry script is located;

### For Windows users do this

```bash
set FLASK_APP = app.py
flask db init
flask db migrate
flask db upgrade
```
### Linux Users do this instead

```bash
export FLASK_APP = app.py
flask db init
flask db migrate
flask db upgrade
```
