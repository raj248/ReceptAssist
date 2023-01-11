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
        self.cursor = self.connection.cursor()

    def user_data(self):
    	self.cursor.execute("select * from USERS")

    	return self.cursor.fetchall()

    def complaint_data(self):
        self.cursor.execute("select * from COMPLAINT_REGISTER")
        return self.cursor.fetchall()
        pass

    def complainer_data(self):
        self.cursor.execute("select * from COMPLAINER_REGISTRATION")
        return self.cursor.fetchall()
        pass



# Server()


# import toga
# from toga.style.pack import LEFT, RIGHT, TOP, ROW, Pack, BOTTOM, COLUMN, CENTER
# def add_user_window(cursor,set_user_table):
#     window = toga.Window(f"Add New User",size=(300,300))
#     content_box = toga.Box(style=Pack(direction=COLUMN,flex=1))

#     # NEW USERNAME
#     user_box = toga.Box(children=[toga.Label("Username ",style=Pack(padding=20))])
#     username = toga.TextInput(placeholder="New Username",style=Pack(padding=10,width=200))
#     user_box.add(username)

#     # NEW PASSWORD
#     pass_box = toga.Box(children=[toga.Label("Password ",style=Pack(padding=20))])
#     password = toga.TextInput(placeholder="New Password",style=Pack(padding=10,width=200))
#     pass_box.add(password)

#     # NEW NAME
#     name_box = toga.Box(children=[toga.Label("Name ",style=Pack(padding=20))])
#     name = toga.TextInput(placeholder="New Name",style=Pack(padding=10,width=200))
#     name_box.add(name)

#     # NEW PHONE
#     phone_box = toga.Box(children=[toga.Label("Phone ",style=Pack(padding=20))])
#     phone = toga.TextInput(placeholder="New Phone",style=Pack(padding=10,width=200))
#     phone_box.add(phone)

#     # NEW TYPE
#     type_box = toga.Box(children=[toga.Label("Type ",style=Pack(padding=20))])
#     type_input= toga.Selection(items=["ADMIN","OPERATOR","USER"],style=Pack(padding=10,width=200))
#     type_box.add(type_input)


#     def _add(btn):
#         if(not username.value):
#             window.info_dialog("Error","Please Enter a Unique Username")
#             return

#         cmd = f'''INSERT INTO USERS VALUE(
#                     "{username.value}",
#                     "{password.value}",
#                     "{name.value}",
#                     "{phone.value}",
#                     "{type_input.value}"
#                     )'''

#         cursor.execute(cmd)
#         set_user_table()

#         btn.window.close()
#         # self.connection.commit()

#     save_btn = toga.Button("Save",on_press=_add)
#     content_box.add(user_box,pass_box,name_box,phone_box,type_box,save_btn)
#     window.content = content_box
#     return window
#     # self.windows.add(window)
#     # window.show()