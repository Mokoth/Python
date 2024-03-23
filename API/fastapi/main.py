from fastapi import FastAPI 
# from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()

# path operations method(get) "/" path

@app.get('/')
def root(): # function
    return {"message": "Hello world"}

@app.get('/posts')
def get_posts():
    return {"data": "this is your posts"}

@app.post('/createposts')
def create_posts(payload: dict = Body(...)):
    print(payload)
    # return {"message": "successfully created posts"}
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}