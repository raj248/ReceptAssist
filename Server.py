import mysql.connector
from textwrap import wrap

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

    def verify_user(self,username,password):
        cmd = f'select * from USERS WHERE Username="{username}" AND Password="{password}"'
        self.cursor.execute(cmd)
        result = self.cursor.fetchall()
        if(len(result)==1):
            return {"Username":result[0][0],"Password":result[0][1],"Name":result[0][2],"Phone":result[0][3],"Type":result[0][4]}
        else:
            return None
    def _wrap_text(self,text,width=25):
        # text = "".join([str(i) for i in range(10)]*10)
        text = "\n".join(wrap(text=text,width=width))
        return text

    def user_data(self,username=""):
        cmd = 'select * from USERS '
        if(username):
            cmd+=f'WHERE Username like "%{username}%"'

        self.cursor.execute(cmd)
        return self.cursor.fetchall()

    def complaint_data(self,complaint_id=""):
        t = None
        cmd = f'select * from COMPLAINT_REGISTER '
        if(complaint_id):
            cmd+=f'WHERE complaint_id like "%{complaint_id}%"'
        self.cursor.execute(cmd)
        t =[(str(i[-1]), i[0],self._wrap_text(i[1]),self._wrap_text(str(i[2])),str(i[3]),i[4],i[5].strftime("%d-%b-%y"),str(i[6]),i[7]) for i in self.cursor.fetchall()]
        return t

    def complainer_data(self,complainer_id=""):
        cmd = f'select * from COMPLAINER_REGISTRATION '
        if (complainer_id):
            cmd+=f'WHERE Complainer_id like "%{complainer_id}%"'        
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
        return t
    def comments_on_complaint(self,complaint_id):
        if( not complaint_id):
            return

        cmd = f"select Comment_text,Name from COMMENTS,USERS where USERS.Username=COMMENTS.Commenter_id and Complaint_id_fk={complaint_id}"
        self.cursor.execute(cmd)

        return self.cursor.fetchall() 


    async def add_user_data(self,data):
        print(data)

    async def add_complaint_data(self,data):
        print(data)

    async def add_complainer_data(self,data):
        print(data)

    async def modify_user(self,data):
        print(data)
    async def modify_complaint(self,data):
        print(data)
    async def modify_complainer(self,data):
        print(data)

    def get_complaint_allotment(self,complaint_id):
        cmd = f'select Name,Status from COMPLAINT_ALLOTMENT,USERS WHERE User=Username and Complaint_id_fk="{complaint_id}"'
        self.cursor.execute(cmd)
        result = self.cursor.fetchall()
        # print("complaint allotments are ",result)
        return result

    def get_unallotted_user(self,complaint_id):
        cmd = f'SELECT Name,Username,Type from USERS where Username not in (select User from COMPLAINT_ALLOTMENT WHERE Complaint_id_fk="{complaint_id}")'
        self.cursor.execute(cmd)
        result = self.cursor.fetchall()
        print("unallotments users are ",result)
        return result

    def allott_complaint(self,username,complaint_id,status):
        if(not username):
            return
        cmd = f'insert into COMPLAINT_ALLOTMENT value ("{username}","{complaint_id}","{status}")'
        self.cursor.execute(cmd)


        