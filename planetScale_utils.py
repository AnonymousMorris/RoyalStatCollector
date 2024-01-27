import os
import mysql.connector
from dotenv import load_dotenv
import time
class pl_db:
    def __init__(self) :
        load_dotenv()
        DB_HOST = os.getenv("DB_HOST")
        DB_USERNAME = os.getenv("DB_USERNAME")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_DATABASE = os.getenv("DB_DATABASE")
        print(DB_HOST, DB_USERNAME, DB_PASSWORD)

        self.connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_DATABASE,
            ssl_verify_identity=True,
            ssl_ca="/etc/ssl/certs/ca-certificates.crt"
        )

        print("Connected to the database", self.connection)
        self.cursor = self.connection.cursor(dictionary=True)

    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        self.connection.close()

    def push_to_fic(self, fics):
        insert_stmt = """
            INSERT INTO fictions ( 
                id, title, description, rating, chapters, retrieved_time, url, followers, pages, views
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
        """

        for fic in fics:
            self.cursor.execute(insert_stmt, (fic["id"],  fic["title"],  fic["description"],  fic['rating'], fic['chapters'], fic['retrieved_time'], fic['url'], fic["followers"], fic["pages"], fic["views"]))

        self.connection.commit()

    # def push_to_rising_stars(self):
    #     self.cursor.execute("""
    #                 CREATE TABLE FICTIONS (
    #                     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #                 );
    #             """)
    #     self.connections.commit()

