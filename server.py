#!/usr/bin/env python
import time
import sqlite3
from contextlib import closing
from flask import Flask, g, jsonify

app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('CUKROWY_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_peak_interval():
    """Return peak interval in seconds."""
    return 60*15


def get_time():
    return int(time.time())


def get_peak():
    count = g.db.execute('select count(*) from wtfs where datetime >= ?',
                         [str(get_time() - get_peak_interval())])
    return count.fetchone()[0]


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/api/peak')
def show_peak():
    return jsonify(peak=get_peak())


@app.route('/api/wtf')
def add_wtf():
    g.db.execute('insert into wtfs (datetime) values (?)', [str(get_time())])
    g.db.commit()
    return jsonify(msg='Added', peak=get_peak())


@app.route('/api/info')
def show_time():
    return jsonify(timestamp=get_time(), peak_interval=get_peak_interval())

if __name__ == '__main__':
    app.run()
