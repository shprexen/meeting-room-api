# Meeting room API

________________

## Prerequisites

- [Python >= 3.8](https://www.python.org/downloads/release/python-3810/)

## Project Structure
- **src** - contains all code related to api.
  - src/config - contains config for db
  - src/routers - contains routers for endpoints
  - src/services - contains services for endpoints
  - src/app.py - is used for initialization of app
  - src/custom_logging.py - contains classes that used for custom logging system
  - src/db.py - is used for initialization of db
  - src/models.py - contains db models
  - src/schemas - contains pydantic schemes of models
- **test** - contains fixtures and tests.
- **.env.example** - example of env-file.
- **logging_config.json** - logging configuration file.
- **run.py** - scripts that runs api
- **requirements.txt** - contains required packages
- **pytest.ini** - pytest configuration file


## Setup How-To

### Before Steps:

1. Clone repository
2. Create .env file in the root from .env.example file.

### Local Run:
1. Create virtual environment - `python -m venv venv`
2. Activate venv - `source venv/bin/activate`
3. Install required packages - `pip install -r requirements.txt`
4. Run api -`python run.py`.
5. Run tests - `pytest`
