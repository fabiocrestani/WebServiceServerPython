#!/bin/bash
export FLASK_DEBUG=1
FLASK_APP=src/server.py flask run --host=0.0.0.0
