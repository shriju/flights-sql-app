import mysql.connector

try:
    conn= mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='sana'

    )
    mycursor= conn.cursor()
    print("Connection Established")

except:
    print("Connection Error")