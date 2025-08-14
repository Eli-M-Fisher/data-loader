import mysql.connector

class DataLoader:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )



    def get_all_data(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM data;")
        result = cursor.fetchall()
        cursor.close()
        return result