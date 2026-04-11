import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host= "localhost",
        user = "root",
        password = "Maninder@0911",
        database = "sales_dashboard"
    )