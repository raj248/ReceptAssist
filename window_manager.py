import toga
from toga.style.pack import LEFT, RIGHT, TOP, ROW, Pack, BOTTOM, COLUMN, CENTER, JUSTIFY,BOLD
from toga.colors import rgb,RED
from textwrap import wrap
class Window_Manager():
    def __init__(self,_self):
        self.server = _self.server
        self.cursor = _self.server.cursor
        self.connection = _self.server.connection

        self.user = _self.user

        self.user_table = _self.user_table
        self.complaint_table = _self.complaint_table
        self.complainer_table = _self.complainer_table

        self.add_comment = _self.add_comment
        self.comment_detail = _self.comment_detail
        self.complaint_details = _self.complaint_details

        self.set_user_table = _self.set_user_table
        self.set_complaint_table = _self.set_complaint_table
        self.set_complainer_table = _self.set_complainer_table

        self.modify_user = _self.modify_user
        self.modify_complaint = _self.modify_complaint
        self.modify_complainer = _self.modify_complainer

        self.delete_user = _self.delete_user
        self.delete_complaint = _self.delete_complaint
        self.delete_complainer = _self.delete_complainer

        self.allott_complaint = _self.allott_complaint
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


        async def _add(btn):
            if(not username.value):
                window.info_dialog("Error","Please Enter a Unique Username")
                return
            result = await self.server.add_user_data({"Username":username.value,"Password":password.value,"Name":name.value,"Phone":phone.value,"Type":type_input.value})

            self.set_user_table()
            btn.window.close()
            # self.connection.commit()

        save_btn = toga.Button("Save",on_press=_add)
        content_box.add(user_box,pass_box,name_box,phone_box,type_box,save_btn)
        window.content = content_box
        return window

    def add_complaint_window(self):
        window = toga.Window(f"Add New Complaint",size=(550,450))
        content_box = toga.Box(id="content_box",style=Pack(direction=COLUMN,flex=1))

        # title,detail,proof_imgfile
        title_box = toga.Box(children=[toga.Label("Title ",style=Pack(padding=10))])
        title = toga.TextInput(placeholder="e.g. Problem/Reason",style=Pack(padding=10,width=200))
        title_box.add(title)

        detail_box = toga.Box(children=[toga.Label("Detail ",style=Pack(flex=1,padding=10))])
        detail = toga.MultilineTextInput(placeholder="e.g. the complainer said...",style=Pack(flex=6,padding=(0,20,10,0)))
        detail_box.add(detail)

        # proof_img_file --> choose_file_dialog
        proof_box = toga.Box()
        file = toga.Label("Proof img file ",style=Pack(padding=20))
        
        async def _choose(btn):
            text = await window.open_file_dialog("Choose img")
            file.text = text

        proof_img_file = toga.Button("choose",on_press=_choose,style=Pack(padding=10))
        proof_box.add(file,proof_img_file)

        # is_approved_by_admin,complainer_id
        is_approved_by_admin = toga.Switch("Is Approved By Admin",style=Pack(width=250,padding=(0,0,10,20)))

        complainer_box = toga.Box(style=Pack(direction=COLUMN))
        complainer_id = toga.TextInput(placeholder='Search by Email',on_change=self.verify_complainer,style=Pack(padding=(0,10,20,20),width=200))
        complainer_box.add(toga.Label("Complainer Email",style=Pack(padding=(0,20,10,20))))


        search_select = toga.Selection(style=Pack(padding=(0,20,20,20),width=400))
        complainer_box.add(complainer_id,search_select)


        async def _add(btn):
            if(not title.value):
                window.info_dialog("Error","Please Enter a Title")
                return
            data = {"Title":title.value,"Detail":detail.value,"File":file.text,"Complainer_id":complainer_id,"is_approved_by_admin":is_approved_by_admin.value}
            result = await self.server.add_complaint_data(data)

            self.set_complaint_table()
            btn.window.close()
            self.connection.commit()
        save_btn = toga.Button("Save",on_press=_add)
        content_box.add(title_box,detail_box,proof_box,is_approved_by_admin,complainer_box,save_btn)
        window.content = content_box
        return window

        pass

    def add_complainer_window(self):
        window = toga.Window(f"Add New Complainer",size=(300,300))
        content_box = toga.Box(style=Pack(direction=COLUMN,flex=1))

        name_box = toga.Box(children=[toga.Label("Name ",style=Pack(padding=20))])
        name = toga.TextInput(placeholder="e.g. Tiwari",style=Pack(padding=10,width=200))
        name_box.add(name)

        email_box = toga.Box(children=[toga.Label("Email ",style=Pack(padding=20))])
        email = toga.TextInput(placeholder="e.g. Tiwari@cooking.com",style=Pack(padding=10,width=200))
        email_box.add(email)

        def _add(btn):
            if(not name.value):
                window.info_dialog("Error","Please Enter a Unique Username")
                return

            data = {"Name":name.value,"Email":email.value}
            self.server.add_complainer_data(data)
            self.set_complainer_table()

            btn.window.close()
            self.connection.commit()

        save_btn = toga.Button("Save",on_press=_add)
        content_box.add(name_box,email_box,save_btn)
        window.content = content_box
        return window
        pass


    def user_details_window(self):
        detail_window = toga.Window("User Details",size=(320,240))

        detail_box = toga.Box(style=Pack(direction=COLUMN,padding=20))

        data = self.server.user_data(self.user_table.selection.Username)

        user_label = toga.Label("Username : "+data[0][0])
        pass_label = toga.Label("Password : "+data[0][1])
        name_label = toga.Label("Name     : "+data[0][2])
        phone_label = toga.Label("Phone   : "+data[0][3])
        type_label = toga.Label("Type     : "+data[0][4])

        detail_box.add(user_label)
        detail_box.add(pass_label)
        detail_box.add(name_label)
        detail_box.add(phone_label)
        detail_box.add(type_label)


        def _modify(cmd):
            self.modify_user(data[0][0])
            detail_window.close()
        def _delete(cmd):
            self.delete_user(data[0][0])
            detail_window.close()

        detail_window.toolbar.add(
                                toga.Command(_modify,"Modify",tooltip="Modify User"),
                                toga.Command(_delete,"Delete",tooltip="Delete User")
                                )

        detail_window.content = detail_box
        return detail_window

    def complaint_details_window(self):
        data = self.server.complaint_data(self.complaint_table.selection.ID)

        detail_window = toga.Window(title=data[0][1],size=(320,240))
        detail_box = toga.Box(style=Pack(direction=COLUMN,padding=20))

        allotments = self.server.get_complaint_allotment(complaint_id=data[0][0])

        # id_label = toga.Label("Complaint ID : "+data[0][0])
        # title_label = toga.Label("Title : "+data[0][1])
        detail_label = toga.Label("Detail : "+data[0][2])
        image_label = toga.Label("\nProof Image File : "+data[0][3])

        complainer_name,complainer_email = self.server.complainer_data(data[0][4])[0][1:3]
        # complainer_label = toga.Label("Complainer   : "+data[0][4])
        complainer_label = toga.Label("\nComplainer Name : %s\nComplainer Email : %s\n"%(complainer_name,complainer_email))

        admin_approval_label = toga.Label("Admin Approval     : "+data[0][5])
        date_label = toga.Label("Complaint Date     : "+data[0][6])
        time_label = toga.Label("Complaint Time     : "+data[0][7])
        timestamp_label = toga.Label("Complaint Timestamp     : "+data[0][8])

        allotment_label = toga.Label('Allotted To',style=Pack(text_align=CENTER,font_weight=BOLD,font_size=18))
        allott_table = toga.Table(["Name","Status"],data=allotments,missing_value="None")

        detail_box.add(
                    # id_label,
                    # title_label,
                    detail_label,
                    image_label,
                    complainer_label,
                    admin_approval_label,
                    date_label,
                    time_label,
                    timestamp_label,
                    allotment_label,
                    allott_table
                    )
        def _comment(cmd):
            self.comment_detail(data[0][0])
        def _modify(cmd):
            self.modify_complaint(data[0][0])
            detail_window.close()
        def _delete(cmd):
            self.delete_complaint(data[0][0])
        async def _allot(cmd):
            self.allott_complaint(data[0][0])
            detail_window.close()
            # self.complaint_details()
        # detail_box.add(toga.Button("Comments",on_press=self.comment_detail))
        # detail_box.add(toga.Button("Modify",on_press=self.modify_complaint))
        # detail_box.add(toga.Button("Delete",on_press=self.delete_complaint))

        detail_window.toolbar.add(toga.Command(_comment,"Comments",tooltip="Comments of this Complaint"),
                                toga.Command(_modify,"Modify",tooltip="Modify Complaint"),
                                toga.Command(_delete,"Delete",tooltip="Delete Complaint"),
                                toga.Command(_allot,"Allot",tooltip="Allot Complaint")
                                )

        detail_window.content = detail_box
        return detail_window

    def complainer_details_window(self):
        detail_window = toga.Window("Complainer Details",size=(400,240))

        detail_box = toga.Box(style=Pack(direction=COLUMN,padding=20))

        data = self.server.complainer_data(self.complainer_table.selection.ID)

        id_label = toga.Label("Complainer ID : "+data[0][0])
        name_label = toga.Label("Name : "+data[0][1])
        email_label = toga.Label("Email : "+data[0][2])
        date_label = toga.Label("Registration Date     : "+data[0][3])
        time_label = toga.Label("Registration Time     : "+data[0][4])
        timestamp_label = toga.Label("Registration Timestamp     : "+data[0][5])

        detail_box.add(id_label,name_label,email_label,date_label,time_label,timestamp_label)

        # detail_box.add(toga.Button("Modify",on_press=self.modify_complainer))
        # detail_box.add(toga.Button("Delete",on_press=self.delete_complainer))

        def _modify(cmd):
            self.modify_complainer(data[0][0])
            detail_window.close()
        def _delete(cmd):
            self.delete_complainer(data[0][0])
 
        detail_window.toolbar.add(
                                toga.Command(_modify,"Modify",tooltip="Modify Complainer"),
                                toga.Command(_delete,"Delete",tooltip="Delete Complainer")
                                )


        detail_window.content = detail_box
        return detail_window


    def modify_user_window(self,username):
        data = self.server.user_data(username)[0]
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

        async def _modify(btn):
            updated_data = {}
            if(not new_username.value):
                updated_data["Username"] = data[0]
            else:
                updated_data["Username"] = new_username.value

            if(not new_password.value):
                updated_data["Password"] = data[1]
            else:
                updated_data["Password"] = new_password.value

            if(not new_name.value):
                updated_data["Name"] = data[2]
            else:
                updated_data["Name"] = new_name.value

            if(not new_phone.value):
                updated_data["Phone"] = data[3]
            else:
                updated_data["Phone"] = new_phone.value

            if(not new_type.value):
                updated_data["Username"] = data[4]
            else:
                updated_data["Username"] = new_type.value

            # cmd = f'''UPDATE USERS 
            #             SET Username="{new_username.value}", 
            #             Password="{new_password.value}",
            #             Name="{new_name.value}",
            #             Phone="{new_phone.value}",
            #             Type="{new_type.value}"
            #             WHERE Username="{data[0]}"'''
            result = await self.server.modify_user(updated_data)
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

    def modify_complaint_window(self,data):
        data = self.server.complaint_data(data)[0]
        window = toga.Window(f"Modify Complaint {data[0]}",size=(500,400))
        content_box = toga.Box(style=Pack(direction=COLUMN,flex=1))

        # NEW Title
        title_box = toga.Box(children=[toga.Label("Title ",style=Pack(padding=20))])
        title = toga.TextInput(placeholder="New Title",style=Pack(padding=10,width=200))
        title_box.add(title)
        
        # NEW Detail
        detail_box = toga.Box(children=[toga.Label("Detail ",style=Pack(padding=20))])
        detail = toga.MultilineTextInput(placeholder="New Detail",style=Pack(padding=10,width=400))
        detail_box.add(detail)

        proof_box = toga.Box()

        file = toga.Label(data[3],style=Pack(padding=20))
        text = ""
        async def _choose(btn):
            try:
                file.text = await window.open_file_dialog("Choose img")
            except:
                pass

        proof_img_file = toga.Button("choose",on_press=_choose,style=Pack(padding=10,width=100))
        proof_box.add(file,proof_img_file)

        complainer_box = toga.Box(style=Pack(direction=COLUMN),children=[toga.Label("Complainer ID",style=Pack(padding=20))])
        complainer_id = toga.TextInput(placeholder='Search by Email',on_change=self.verify_complainer,style=Pack(padding=(0,10,20,20),width=200))

        search_select = toga.Selection(style=Pack(padding=(0,20,20,20),width=400))
        complainer_box.add(complainer_id,search_select)

        is_approved_by_admin = toga.Switch("Is Approved By Admin")
        is_approved_by_admin.value = False if data[5]=="False" else True

        async def _modify(btn):
            complainer_id = data[0]
            updated_data = {}
            if(not title.value):
                updated_data["Title"] = data[1]
            else:
                updated_data["Title"] = title.value

            if(not detail.value):
                updated_data["Detail"] = data[2]
            else:
                updated_data["Detail"] = detail.value

            if(not file.text):
                updated_data["Proof_img_file"] = data[3]
            else:
                updated_data["Proof_img_file"] = detail.value

            if(not complainer_id):
                 updated_data["Complainer_id_fk"] = data[4]
            else:
                 updated_data["Complainer_id_fk"] = complainer_id

            # cmd = f'''UPDATE COMPLAINT_REGISTER 
            #             SET Complaint_title="{title.value}", 
            #             Complaint_detail="{detail.value}",
            #             Proof_img_file="{file.text}",
            #             Complainer_id_fk="{complainer_id}",
            #             Is_approved_by_admin="{is_approved_by_admin.value}"
            #             WHERE Complaint_id="{data[0]}"'''

            result = await self.server.modify_complaint(updated_data)
            self.set_complaint_table()

            self.connection.commit()
            # btn.window.info_dialog("Result","Operation Successful")
            btn.window.close()

        save_btn = toga.Button("Save",on_press=_modify)
        content_box.add(title_box,detail_box,proof_box,is_approved_by_admin,complainer_box,save_btn)
        window.content = content_box
        
        return window    
        
        # self.windows.add(window)
        # window.show()
        # widgets.window.close()
        pass

    def modify_complainer_window(self,complainer_id):

        data = self.server.complainer_data(complainer_id)[0]
        window = toga.Window(f"Modify Complainer {data[0]}",size=(240,200))
        content_box = toga.Box(style=Pack(direction=COLUMN,flex=1))

        # NEW Name
        name_box = toga.Box(children=[toga.Label("Name ",style=Pack(padding=20))])
        name = toga.TextInput(placeholder="New Name",style=Pack(padding=10,width=200))
        name_box.add(name)
        
        # NEW Email
        email_box = toga.Box(children=[toga.Label("Email ",style=Pack(padding=20))])
        email = toga.TextInput(placeholder="New Email",style=Pack(padding=10,width=200))
        email_box.add(email)

       
        async def _modify(btn):
            updated_data = {}
            if(not name.value):
                updated_data["Name"] = data[1]
            else:
                updated_data["Name"] = name.value

            if(not email.value):
                updated_data["Email"] = data[2]
            else:
                updated_data["Email"] = email.value 

            
            # cmd = f'''UPDATE COMPLAINER_REGISTRATION 
            #             SET Name="{name.value}", 
            #             Email="{email.value}" 
            #             WHERE Complainer_id={data[0]}'''

            result = await self.server.modify_complainer(data)
            self.set_complainer_table()
            
            # self.connection.commit()
            # btn.window.info_dialog("Result","Operation Successful")
            btn.window.close()

        save_btn = toga.Button("Save",on_press=_modify)
        content_box.add(name_box,email_box,save_btn)
        window.content = content_box
        
        return window    


    def verify_complainer(self,txt_input):
        cmd = f'Select * from COMPLAINER_REGISTRATION WHERE (Email like"%{txt_input.value}%" OR Name like"%{txt_input.value}%")'
        self.cursor.execute(cmd)
        selection = txt_input.parent.children[2]
        items = [i[0]+" "+i[1] for i in self.cursor.fetchall()]
        selection.items = items
        pass


    def _wrap_text(self,text,width=70):
        # text = "".join([str(i) for i in range(10)]*10)
        text = "\n".join(wrap(text=text,width=width))
        return text

    def comment_window(self,complaint_id):
        window = toga.Window("Comments",size=(320,240))
        # complaint_id = 1;
        data = self.server.comments_on_complaint(complaint_id)
        comment_box = toga.Box(style=Pack(text_align=JUSTIFY,direction=COLUMN))
        for i in data:
            text = self._wrap_text(i[0]) + '\n ~# '+i[1]
            comment_box.add(toga.Label(text,style=Pack( padding=(0,30,10,30)))) 

        def _add_comment(btn):
            self.add_comment(complaint_id,btn.parent.children[0].value)
            self.comment_detail(complaint_id=complaint_id)
            btn.window.close()

        scroll_content = toga.Box(style=Pack(direction=COLUMN,alignment=RIGHT),
            children=[
                comment_box,
                toga.Box(style=Pack(alignment=CENTER,flex=1),
                    children=[
                        toga.TextInput(placeholder="Comment....",style=Pack(width=300,padding=20)),
                        toga.Button("Add",on_press=_add_comment,style=Pack(padding=20))
                        ])
                ])

        scroll = toga.ScrollContainer(content=scroll_content,horizontal=False)
        window.content = scroll
        return window

    def add_comment_window(self):
        pass

    def allott_complaint_window(self,complaint_id):
        window = toga.Window(title="Allott Complaint")
        content_box = toga.Box(style=Pack(direction=COLUMN),
            children=[
                toga.Label("Select A User",style=Pack(text_align=CENTER))
                ]
            )
        table = toga.Table(["Name","Username","Type"],accessors = ['Name','Username','Type'],missing_value="None")
        status_selection = toga.Selection(items=["in_process",'closed','open','resolved'])
        _complaint_id = complaint_id
        async def _save(btn):
            complaint_id = _complaint_id
            uid = table.selection.Username
            status = status_selection.value

            self.server.allott_complaint(uid,complaint_id,status)
            # self.connection.commit()
            window.close()

        table.data = self.server.get_unallotted_user(complaint_id)

        content_box.add(table,status_selection,toga.Button("OK",on_press=_save))
        window.content = content_box
        return window