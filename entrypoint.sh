#!/bin/sh
export AUTODETECT=true
if [ $AUTODETECT = true ]; then
    python so.py
else
    python app.py
fi