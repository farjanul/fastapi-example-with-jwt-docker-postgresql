#!/bin/bash
sleep 5
alembic upgrade head
uvicorn main:app --reload --host 0.0.0.0 --port 8000