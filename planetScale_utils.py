import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_DATABASE,
    ssl_verify_identity=True,
    ssl_ca="/etc/ssl/certs/ca-certificates.crt"
)

print("Connected to the database")

cursor = connection.cursor(dictionary=True)

cursor.execute("""
    CREATE TABLE FICTIONS (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    );
""")

connection.commit()

cursor.close()
connection.close()