import mysql.connector

class Server():
    def __init__(self,username="root", password="007281", host="localhost"):
        mydb = mysql.connector.connect(
          host=host,
          user='root',
          password='007281',
          database='zenex_complaint_register'
          )
        self.connection = mydb
        self.cursor = self.connection.cursor(buffered=True)

    def user_data(self,cmd=None):
        if(not cmd):
            cmd = "select * from USERS"

        self.cursor.execute(cmd)
        return self.cursor.fetchall()

    def complaint_data(self,cmd=None):
        t = None
        if(not cmd):
            cmd = "select * from COMPLAINT_REGISTER"
            self.cursor.execute(cmd)
            t =[(str(i[-1]), i[0],i[1][:25]+'...',str(i[2][:25]+'...'),str(i[3]),i[4],i[5].strftime("%d-%b-%y"),str(i[6]),i[7]) for i in self.cursor.fetchall()]

        else:
            self.cursor.execute(cmd)
            t =[(str(i[-1]), i[0],i[1],str(i[2]),str(i[3]),i[4],i[5].strftime("%d-%b-%y"),str(i[6]),i[7]) for i in self.cursor.fetchall()]

        return t
        pass

    def complainer_data(self,cmd=None):
        if(not cmd):
            cmd = "select * from COMPLAINER_REGISTRATION"
        self.cursor.execute(cmd)
        # [('Zedd', 'zed007281@gmail.com', datetime.date(2023, 1, 9), datetime.timedelta(seconds = 69264), '2023-01-09 19:14:24', 1), 
        # ('bear', 'bearFF281@gmail.com', datetime.date(2023, 1, 9), datetime.timedelta(seconds = 69264), '2023-01-09 19:14:24', 2)]
        t = [(str(i[-1]), i[0], i[1], i[2].strftime("%d-%b-%y"), str(i[3]), i[4]) for i in self.cursor.fetchall()]
        return t
    def comment_data(self,cmd=None):
        if(not cmd):
            cmd = "select * from COMMENTS"
        self.cursor.execute(cmd)
        t = [(str(i[-1]), i[0], str(i[1]), i[2],i[3].strftime("%d-%b-%y"),str(i[4]),i[5]) for i in self.cursor.fetchall()]
        # print(t)
        return t
    def comments_on_complaint(self,complaint_id):
        if( not complaint_id):
            return

        cmd = f"select Comment_text,Name from COMMENTS,USERS where USERS.Username=COMMENTS.Commenter_id and Complaint_id_fk={complaint_id}"
        self.cursor.execute(cmd)

        return self.cursor.fetchall() 

    
