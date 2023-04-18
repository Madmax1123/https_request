import mysql.connector
class all_info:
      class dbs:
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="basedata"
        )

        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS basedata")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emails 
            (id INT AUTO_INCREMENT PRIMARY KEY, 
            email VARCHAR(50), 
            password VARCHAR(25), 
            response TEXT)
            """
        ) 
        data = {
            'email' : 'admin@admin.com',
            'password' : '12345' 
        }

        headers = {
            'Content-Type': 'application/json',
            'X-eBirdApiToken': ''
        }
     
