#!/usr/bin/env bash
fi
(cd src/main; gunicorn main.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"