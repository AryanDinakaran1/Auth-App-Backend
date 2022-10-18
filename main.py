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

# http://localhost:3000

@app.get('/')
async def get_users():
    users = session.query(Users)
    usersDict = {}

    for user in users:
        usersDict[int(user.id)] = {
            'email': user.email,
            'username' : user.username,
        }

    return usersDict

@app.post('/signup')
async def signup(username: str = Form(...), email: str = Form(...), password: str = Form(...)):

    
    password = hashlib.sha256(password.encode()).hexdigest()

    newUser = Users(username=username, email=email, password=password)
    session.add(newUser)
    session.commit()

    # Write code to redirect to an external page and test it

    return {
        'username' : username,
        'email' : email,
        'password' : password
    }