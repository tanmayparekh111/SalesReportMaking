import mysql.connector
import pandas as pd



def FatchTables():
    '''
    This function is used to fatch the availavle tablenames in the given database.
    '''
    db = mysql.connector.connect(
    host="localhost",  
    user="root",  
    password="rootroot",  
    database="interview"
    )

    query = f"show tables"

    df = pd.read_sql_query(query,db)
    TableNames = df["Tables_in_interview"].to_list()

    return TableNames
    


def FatchData(TableName):
    '''
    this function is used to fatch the table from the given table name
    '''

    db = mysql.connector.connect(
    host="localhost",  
    user="root",  
    password="rootroot",  
    database="interview"
    )

    query = f"SELECT * FROM {TableName}"


    df = pd.read_sql_query(query, db)

    db.close()

    return df