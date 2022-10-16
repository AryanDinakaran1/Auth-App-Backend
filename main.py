import hashlib 
import mysql.connector
from decouple import config

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

con = mysql.connector.connect(
    host = config('HOST'),
    user = config('USER'),
    port = config('PORT'),
    password = config('PASSWORD'),
    database = config('DATABASE')
)

mycursor = con.cursor()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get('/')
async def get_users():
    mycursor.execute('SELECT * FROM Users')
    results = mycursor.fetchall()

    print(results)

    return {}

@app.post('/signup')
async def signup(username: str = Form(...), first_name: str = Form(...), last_name: str = Form(...), password: str = Form(...)):
    insertStatement = 'INSERT INTO Users (username, first_name, last_name, password) VALUES (%s,%s,%s,%s)'
    password = hashlib.sha256(password.encode()).hexdigest()
    val = (username, first_name, last_name, password)

    mycursor.execute(insertStatement, val)

    con.commit()

    # Write code to redirect to an external page and test it

    return {
        'username' : username,
        'first_name' : first_name,
        'last_name' : last_name,
        'password' : password
    }