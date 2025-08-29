FROM python:3.9-slim

WORKDIR /app

COPY . .

CMD ["python", "scheduler.py"]
# Adding a comment to make a change in this file so i can make a push to github 