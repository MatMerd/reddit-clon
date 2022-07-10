#! /usr/bin/env bash

alembic upgrade head

gunicorn -k uvicorn.workers.UvicornWorker -c ./gunicorn_conf.py run:app