import mysql.connector

def login(username="", password="", host="localhost"):
  try:
    mydb = mysql.connector.connect(
      host=host,
      user='root',
      password='007281',
      database='zenex_query'
      )

    cur = mydb.cursor()

    cur.execute(f'select * from USERS WHERE Username="{username}" AND Password="{password}"')
    row = cur.fetchall()
    if(len(row)==1):
      return row[0][2]
  except Exception as e:
    return None



print(login("root",'abc123'))