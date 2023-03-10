# git push -u origin master
import toga,sys
from toga.style.pack import LEFT, RIGHT, TOP, ROW, Pack, BOTTOM, COLUMN, CENTER
from Server import Server
from window_manager import Window_Manager 

# CONSTANT VARIABLES

USER_HEADING = ['Username','Password','Name','Phone','Type']
USER_ACCESSORS = USER_HEADING

COMPLAINT_HEADING = ["ID","Title","Detail","Files","Complainer ID","Admin Approval","Date","Time","Timestamp"]
COMPLAINT_ACCESSORS = COMPLAINT_HEADING

COMPLAINER_HEADING = ["ID","Name","Email","Regis. Date","Regis. Time","Regis. Timestamp"]
COMPLAINER_ACCESSORS = COMPLAINER_HEADING

class Dashboard(toga.App):
    def startup(self):

        # self.Cursor()
        self.user = {"Name":"Bell","Type":"ADMIN","UID":"root"}

        self.main_window = toga.MainWindow(title = "Dashboard",size=(900,550))
        self.main_box = toga.Box()
        button_box = toga.Box(style=Pack(direction=COLUMN,flex=1))

        self.add_btn = toga.Button('Add',on_press=self.add_user)
        self.detail_btn = toga.Button('Details',on_press=self.user_details)
        self.action_btn = toga.Button('Action',on_press=self.action)

        button_box.add(self.add_btn)
        button_box.add(self.detail_btn)
        button_box.add(self.action_btn)
        self.main_box.add(button_box)


        group = toga.Group("Functions")

        user_cmd = toga.Command(self.set_user_table,"User",tooltip="Modify Users",group=group)
        record_cmd = toga.Command(self.set_complainer_table,"Complainer",tooltip="Modify Records",group=group)
        complaint_cmd = toga.Command(self.set_complaint_table,"Complaint",tooltip="Modify Complaint",group=group)

        self.main_window.toolbar.add(user_cmd,record_cmd,complaint_cmd)
        self.user_table = toga.Table(USER_HEADING, accessors = USER_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.complaint_table = toga.Table(COMPLAINT_HEADING, accessors = COMPLAINT_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.complainer_table = toga.Table(COMPLAINER_HEADING, accessors = COMPLAINER_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)


        self.main_window.content = self.main_box
        self.server = Server()
        self.login()
        # self.initialize(self.user)

    def login(self):
        window = toga.Window(title="Login")
        content_box = toga.Box()

        user_input = toga.TextInput(placeholder="Username")
        pass_input = toga.PasswordInput(placeholder="Password")
        def _verify(btn):
            result = self.server.verify_user(user_input.value,pass_input.value)
            if(result):
                self.user = result
                self.initialize(self.user)
                window.close()
                return
            else:
                # quit()
                window.close()
                sys.exit()
            pass
        login_button = toga.Button("Log In",on_press=_verify)

        username = toga.Label("Username")
        password = toga.Label("Password")
        status = toga.Label("")

        content_box.add(username)
        content_box.add(user_input)
        content_box.add(password)
        content_box.add(pass_input)
        content_box.add(login_button)
        content_box.add(status)

        content_box.style.update(direction=COLUMN)
        user_input.style.update(padding_bottom=20)
        pass_input.style.update(padding_bottom=20)
        login_button.style.update(padding_bottom=20)
        status.style.update(text_align=CENTER)

        window.content = content_box
        self.windows.add(window)
        window.show()

    def initialize(self,user):
        self.user = user
        self.window_manager = Window_Manager(self)
        self.set_user_table()
        self.main_window.show()

    def set_user_table(self,widgets=None):
        self.add_btn.on_press = self.add_user
        self.detail_btn.on_press = self.user_details


        self.main_box.remove(self.complaint_table,self.complainer_table)
        # self.table = toga.Table(USER_HEADING, accessors = USER_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.user_table.data = self.server.user_data()
        self.main_box.add(self.user_table)
        # self.main_window.refresh()

    def set_complaint_table(self,widgets=None):
        self.add_btn.on_press = self.add_complaint
        self.detail_btn.on_press = self.complaint_details

        self.main_box.remove(self.user_table,self.complainer_table)
        # self.table = toga.Table(COMPLAINT_HEADING, accessors = COMPLAINT_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.complaint_table.data = self.server.complaint_data()
        self.main_box.add(self.complaint_table)

    def set_complainer_table(self,widgets=None):
        self.add_btn.on_press = self.add_complainer
        self.detail_btn.on_press = self.complainer_details
        self.main_box.remove(self.user_table,self.complaint_table)
        # self.table = toga.Table(COMPLAINER_HEADING, accessors = COMPLAINER_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.complainer_table.data = self.server.complainer_data()
        self.main_box.add(self.complainer_table)


    def action(self,btn):
        self.main_window.info_dialog('Notice','Action Button is Pressed!')
        return

    def add_user(self,widgets):
        window = self.window_manager.add_user_window()
        self.windows.add(window)
        window.show()
        return
        
    def add_complaint(self, widgets):
        window = self.window_manager.add_complaint_window()
        self.windows.add(window)
        window.show()
        pass

    def add_complainer(self,widgets):
        window = self.window_manager.add_complainer_window()
        self.windows.add(window)
        window.show()
        pass



    def user_details(self,widgets):
        if(not self.user_table.selection):
            return
        detail_window = self.window_manager.user_details_window()

        self.windows.add(detail_window)
        detail_window.show()

    def complaint_details(self,widgets=None):
        if(not self.complaint_table.selection):
            return
        detail_window = self.window_manager.complaint_details_window()
        self.windows.add(detail_window)
        detail_window.show()
        pass

    def complainer_details(self,widgets=None):
        if(not self.complainer_table.selection):
            return
        detail_window = self.window_manager.complainer_details_window()
        self.windows.add(detail_window)
        detail_window.show()
        pass


    def modify_user(self,username):
        window = self.window_manager.modify_user_window(username)
        
        self.windows.add(window)
        window.show()
        pass

    def modify_complaint(self,complaint_id):
        window = self.window_manager.modify_complaint_window(complaint_id)
        self.windows.add(window)
        window.show()
        # widgets.window.close()
        pass

    def modify_complainer(self,complainer_id):
        window = self.window_manager.modify_complainer_window(complainer_id)
        self.windows.add(window)
        window.show()
        pass


    def delete_user(self,username):

        def _delete(any_,result):
            if(not result):
                return

            cmd = f'DELETE From USERS WHERE Username="{username}"'
            self.server.cursor.execute(cmd)
            self.set_user_table()

            # self.connection.commit()

        self.main_window.confirm_dialog("CONFIRM",f"Delete User '{username}'",on_result=_delete)
        return

    def delete_complaint(self,complaint_id):

        def _delete(any_,result):
            if(not result):
                return
            cmd = f'DELETE From COMPLAINT_REGISTER WHERE Complaint_id="{complaint_id}"'
            self.server.cursor.execute(cmd)
            self.set_complaint_table()

            # widgets.window.info_dialog(f"Deleted {data[0]}","")
            # self.connection.commit()

        self.main_window.confirm_dialog("CONFIRM",f"Delete Complaint",on_result=_delete)
        widgets.window.close()
        return

        pass
        
    def delete_complainer(self,complainer_id):

        def _delete(any_,result):
            if(not result):
                return
            cmd = f'DELETE From COMPLAINER_REGISTRATION WHERE Complainer_id="{complainer_id}"'
            self.server.cursor.execute(cmd)
            self.set_complainer_table()

            # widgets.window.info_dialog(f"Deleted {data[0]}","")
            # self.connection.commit()

        self.main_window.confirm_dialog("CONFIRM","Delete Complainer ",on_result=_delete)
        return

        pass

    def add_comment(self,complaint_id,text):
        cmd = f'''insert into COMMENTS(Comment_text,Complaint_id_fk,Commenter_id,Date,Time,Timestamp) value (
                    "{text}",
                    {complaint_id},
                    "{self.user["UID"]}",
                    curdate(),curtime(),current_timestamp()
                    )'''
        self.server.cursor.execute(cmd)
        self.server.connection.commit()


    def comment_detail(self, complaint_id=None):
        if(not complaint_id):
            return
        window = self.window_manager.comment_window(complaint_id)
        self.windows.add(window)
        window.show()

    def allott_complaint(self,complaint_id=None):
        if(not complaint_id):
            return
        window = self.window_manager.allott_complaint_window(complaint_id)
        self.windows.add(window)
        window.show()

        pass





Dashboard("App",'support.it').main_loop()