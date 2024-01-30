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

    def delete_duplicates_in_fictions(self):
        insert_stmt = """
            DELETE FROM fictions 
            WHERE NOT EXISTS (
                SELECT 1 
                FROM fictions AS t2
                WHERE fictions.id = t2.id
                      fictions.title = t2.title
                      fictions.description = t2.description
                      fictions.rating = t2.rating
                      fictions.chapters = t2.chapters
                      fictions.retrieved_time > t2.retrieved_time
                      fictions.url = t2.url
                      fictions.followers = t2.followers
                      fictions.pages = t2.pages
                      fictions.views = t2.views
            )
        """
    def push_to_rating(self, fics, category):
        insert_stmt = """
            INSERT INTO rising_stars ( 
                id, retrieved_time, category, placement
            ) VALUES (
                %s, %s, %s, %s
            );
        """

        for fic in fics:
            self.cursor.execute(insert_stmt, (fic["id"], fic["retrieved_time"], category, fic["placement"]))

        self.connection.commit()

