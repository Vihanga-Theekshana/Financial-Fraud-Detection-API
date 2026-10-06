from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)
POSTGRE_PASSWORD = os.getenv("POSTGRE_PASSWORD")
conn = psycopg2.connect(
    dbname="financial_db", 
    user="postgres",
    password=POSTGRE_PASSWORD, 
    host="localhost",
    port="5432"
)

conn.autocommit = True
#when we use cursor we can work inside database

cursor = conn.cursor()

