#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
export PYTHONPATH="${PYTHONPATH}:/${DIR}/app"

export FLASK_APP=app
flask db init
flask db migrate -m "users table"
flask db upgrade

flask run --port=8000