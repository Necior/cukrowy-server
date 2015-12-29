# server

`server` is a backend part of the _cukrowy_ project. It has been crafted using Python and Flask to provide JSON API for its clients. `server` is under (heavy) development.

## Installation

```
$ git clone git@github.com:Necior/cukrowy-server.git
$ cd server
$ virtualenv cukrowy
$ source cukrowy/bin/activate
$ pip install -r requirements.txt
```

(To exit virtual environment, type `deactivate`.)

## Setting up

Edit `config.py` according to your needs. Then, create the database by running `python init_db.py` (**it will remove your current database**).

You can also provide your own configuration file with environment variable `CUKROWY_SETTINGS`, for example:

```
$ export CUKROWY_SETTINGS=my_config.py
$ python server.py
```

## Running

### Development

Activate virtual environment (`source cukrowy/bin/activate`) and run it (`python server.py`).

### Production

Be sure to set the `SECRET_KEY` and turn off the `DEBUG` flag. Deploy according to the [Flask documentation](http://flask.pocoo.org/docs/0.10/deploying/#deployment).

