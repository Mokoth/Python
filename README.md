# Python

## API
mkdir fastapi
cd fastapi && touch main.py

python3 -m venv venv
source venv/bin/activate + you can use to deactivate to disable venv
pip install fastapi[all]

pip freeze - show installed packages

uvicorn main:app --reload

HTTP requests
GET - retrieve data [API server, give me some data]

POST
create a social media post - [API server, here are some data]

title
content

send data from the body - JSON

{
    "title": "Top beaches",
    "content": "check this awesome beaches"
}

In an API, the payload is the data that is sent to the server when an API request is made.