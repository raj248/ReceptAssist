import toga
from toga.style.pack import LEFT, RIGHT, TOP, ROW, Pack, BOTTOM, COLUMN, CENTER

class Window_Manager():
    def __init__(self,_self):
        self.cursor = _self.server.cursor
        self.table = _self.table
        self.set_user_table = _self.set_user_table
        self.set_complaint_table = _self.set_complaint_table
        self.set_complaier_table = _self.set_complainer_table
        self.modify_user = _self.modify_user
        self.delete_user = _self.delete_user
        pass

    def add_user_window(self):
        window = toga.Window(f"Add New User",size=(300,300))
        content_box = toga.Box(style=Pack(direction=COLUMN,flex=1))

        # NEW USERNAME
        user_box = toga.Box(children=[toga.Label("Username ",style=Pack(padding=20))])
        username = toga.TextInput(placeholder="New Username",style=Pack(padding=10,width=200))
        user_box.add(username)

        # NEW PASSWORD
        pass_box = toga.Box(children=[toga.Label("Password ",style=Pack(padding=20))])
        password = toga.TextInput(placeholder="New Password",style=Pack(padding=10,width=200))
        pass_box.add(password)

        # NEW NAME
        name_box = toga.Box(children=[toga.Label("Name ",style=Pack(padding=20))])
        name = toga.TextInput(placeholder="New Name",style=Pack(padding=10,width=200))
        name_box.add(name)

        # NEW PHONE
        phone_box = toga.Box(children=[toga.Label("Phone ",style=Pack(padding=20))])
        phone = toga.TextInput(placeholder="New Phone",style=Pack(padding=10,width=200))
        phone_box.add(phone)

        # NEW TYPE
        type_box = toga.Box(children=[toga.Label("Type ",style=Pack(padding=20))])
        type_input= toga.Selection(items=["ADMIN","OPERATOR","USER"],style=Pack(padding=10,width=200))
        type_box.add(type_input)


        def _add(btn):
            if(not username.value):
                window.info_dialog("Error","Please Enter a Unique Username")
                return

            cmd = f'''INSERT INTO USERS VALUE(
                        "{username.value}",
                        "{password.value}",
                        "{name.value}",
                        "{phone.value}",
                        "{type_input.value}"
                        )'''

            self.cursor.execute(cmd)
            self.set_user_table()

            btn.window.close()
            # self.connection.commit()

        save_btn = toga.Button("Save",on_press=_add)
        content_box.add(user_box,pass_box,name_box,phone_box,type_box,save_btn)
        window.content = content_box
        return window
        # self.windows.add(window)
        # window.show()


    def add_complaint_window(self,cursor,set_complaint_table):
        print("Please Impliment Complaint window!!!")
        pass

    def add_complainer_window(self,cursor,set_complainer_table):
        print("Please Impliment Complainer window!!!")
        pass

    def user_details_window(self):
        # if(not table.selection):
        #     return
        detail_window = toga.Window("User Details",size=(320,240))

        detail_box = toga.Box(style=Pack(direction=COLUMN,padding=20))
        print(self.table,"in wm")

        user_label = toga.Label("Username : "+self.table.selection.Username)
        pass_label = toga.Label("Password : "+self.table.selection.Password)
        name_label = toga.Label("Name     : "+self.table.selection.Name)
        phone_label = toga.Label("Phone   : "+self.table.selection.Phone)
        type_label = toga.Label("Type     : "+self.table.selection.Type)
        detail_box.add(user_label)
        detail_box.add(pass_label)
        detail_box.add(name_label)
        detail_box.add(phone_label)
        detail_box.add(type_label)

        detail_box.add(toga.Button("Modify",on_press=self.modify_user))
        detail_box.add(toga.Button("Delete",on_press=self.delete_user))

        detail_window.content = detail_box
        return detail_window

        # self.windows.add(detail_window)
        # detail_window.show()

    def complaint_details_window(self,table,modify_complaint,delete_complaint):
        print("Please Impliment Complaint detail window!!!")

    def complainer_details_window(self,table,modify_complainer,delete_complainer):
        print("Please Impliment Complainer detail window!!!")

    def modify_user_window(self,data):
        # data = [i.text.split(":")[1].strip() for i in widgets.parent.children[:5]]
        # print(data)
        window = toga.Window(f"Modify User {data[0]}",size=(300,300))
        content_box = toga.Box(style=Pack(direction=COLUMN,flex=1))
        # NEW USERNAME
        user_box = toga.Box(children=[toga.Label("Username ",style=Pack(padding=20))])
        new_username = toga.TextInput(placeholder="New Username",style=Pack(padding=10,width=200))
        user_box.add(new_username)
        
        # NEW PASSWORD
        pass_box = toga.Box(children=[toga.Label("Password ",style=Pack(padding=20))])
        new_password = toga.TextInput(placeholder="New Password",style=Pack(padding=10,width=200))
        pass_box.add(new_password)

        # NEW NAME
        name_box = toga.Box(children=[toga.Label("Name ",style=Pack(padding=20))])
        new_name = toga.TextInput(placeholder="New Name",style=Pack(padding=10,width=200))
        name_box.add(new_name)

        # NEW PHONE
        phone_box = toga.Box(children=[toga.Label("Phone ",style=Pack(padding=20))])
        new_phone = toga.TextInput(placeholder="New Phone",style=Pack(padding=10,width=200))
        phone_box.add(new_phone)

        # NEW TYPE
        type_box = toga.Box(children=[toga.Label("Type ",style=Pack(padding=20))])
        new_type= toga.Selection(items=["ADMIN","OPERATOR","USER"],style=Pack(padding=10,width=200))
        type_box.add(new_type)

        def _modify(btn):
            if(not new_username.value):
                new_username.value = data[0]
            if(not new_password.value):
                new_password.value = data[1]
            if(not new_name.value):
                new_name.value = data[2]
            if(not new_phone.value):
                new_phone.value = data[3]
            if(not new_type.value):
                new_type.value = data[4]

            cmd = f'''UPDATE USERS 
                        SET Username="{new_username.value}", 
                        Password="{new_password.value}",
                        Name="{new_name.value}",
                        Phone="{new_phone.value}",
                        Type="{new_type.value}"
                        WHERE Username="{data[0]}"'''
            self.cursor.execute(cmd)
            self.set_user_table()
            # self.connection.commit()
            # btn.window.info_dialog("Result","Operation Successful")
            btn.window.close()

        save_btn = toga.Button("Save",on_press=_modify)
        content_box.add(user_box,pass_box,name_box,phone_box,type_box,save_btn)
        window.content = content_box
        
        return window    
        
        # self.windows.add(window)
        # window.show()
        # widgets.window.close()
        pass

    def modify_complaint_window(self,data,cursor,set_complaint_table):
        print("Please Impliment modify_complaint_window!!!")

    def modify_complainer_window(self,data,cursor,set_complainer_table):
        print("Please Impliment modify_complainer_window!!!")
