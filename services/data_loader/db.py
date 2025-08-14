import mysql.connector

class DataLoader:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="mydb"
        )



    def get_all_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM data")
        result = cursor.fetchall()
        cursor.close()
        return result