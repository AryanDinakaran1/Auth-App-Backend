import hashlib 
import mysql.connector
from decouple import config

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

from models import Users, session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get('/')
async def get_users():
    pass

@app.post('/signup')
async def signup(username: str = Form(...), first_name: str = Form(...), last_name: str = Form(...), password: str = Form(...)):

    
    password = hashlib.sha256(password.encode()).hexdigest()

    newUser = Users(username=username, first_name=first_name, last_name=last_name, password=password)
    session.add(newUser)
    session.commit()

    # Write code to redirect to an external page and test it

    return {
        'username' : username,
        'first_name' : first_name,
        'last_name' : last_name,
        'password' : password
    }