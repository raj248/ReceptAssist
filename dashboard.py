# git push -u origin master
import toga
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

class Login(toga.App):
    def startup(self):

        # self.Cursor()

        self.main_window = toga.MainWindow(title = "Dashboard",size=(900,550))
        self.main_box = toga.Box()
        button_box = toga.Box(style=Pack(direction=COLUMN,flex=1))

        self.add_btn = toga.Button('Add',on_press=self.add_user)
        self.detail_btn = toga.Button('Details',on_press=self.user_details)
        self.action_btn = toga.Button('Action',on_press=self.action2)

        button_box.add(self.add_btn)
        button_box.add(self.detail_btn)
        button_box.add(self.action_btn)
        self.main_box.add(button_box)


        group = toga.Group("Functions")

        user_cmd = toga.Command(self.set_user_table,"User",tooltip="Modify Users",group=group)
        record_cmd = toga.Command(self.set_complainer_table,"Complainer",tooltip="Modify Records",group=group)
        complaint_cmd = toga.Command(self.set_complaint_table,"Complaint",tooltip="Modify Records",group=group)

        self.main_window.toolbar.add(user_cmd,record_cmd,complaint_cmd)
        self.user_table = toga.Table(USER_HEADING, accessors = USER_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.complaint_table = toga.Table(COMPLAINT_HEADING, accessors = COMPLAINT_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.complainer_table = toga.Table(COMPLAINER_HEADING, accessors = COMPLAINER_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)

        self.server = Server()
        self.window_manager = Window_Manager(self)

        self.set_user_table()
        self.main_window.content = self.main_box
        self.main_window.show()


    def set_user_table(self,widgets=None):
        self.add_btn.on_press = self.add_user
        self.detail_btn.on_press = self.user_details

        print('Setting User Table')
        self.main_box.remove(self.complaint_table,self.complainer_table)
        # self.table = toga.Table(USER_HEADING, accessors = USER_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.user_table.data = self.server.user_data()
        self.main_box.add(self.user_table)
        # self.main_window.refresh()

    def set_complaint_table(self,widgets=None):
        self.add_btn.on_press = self.add_complaint
        self.detail_btn.on_press = self.complaint_details

        print("Setting Complaint Table")
        self.main_box.remove(self.user_table,self.complainer_table)
        # self.table = toga.Table(COMPLAINT_HEADING, accessors = COMPLAINT_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.complaint_table.data = self.server.complaint_data()
        self.main_box.add(self.complaint_table)

    def set_complainer_table(self,widgets=None):
        self.add_btn.on_press = self.add_complainer
        self.detail_btn.on_press = self.complainer_details
        print("Setting Complainer Table")
        self.main_box.remove(self.user_table,self.complaint_table)
        # self.table = toga.Table(COMPLAINER_HEADING, accessors = COMPLAINER_ACCESSORS,missing_value="None",style=Pack(flex=10),on_select=None)
        self.complainer_table.data = self.server.complainer_data()
        self.main_box.add(self.complainer_table)


    def action2(self):
        print('action2')
        return

    def add_user(self,widgets):
        # print(widgets.on_press)
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

    def complaint_details(self,widgets):
        if(not self.complaint_table.selection):
            return
        detail_window = self.window_manager.complaint_details_window()
        self.windows.add(detail_window)
        detail_window.show()
        pass

    def complainer_details(self,widgets):
        if(not self.complainer_table.selection):
            return
        detail_window = self.window_manager.complainer_details_window()
        self.windows.add(detail_window)
        detail_window.show()
        pass


    def modify_user(self,widgets):
        data = [i.text.split(":")[1].strip() for i in widgets.parent.children[:5]]
        window = self.window_manager.modify_user_window(data[0])
        
        self.windows.add(window)
        window.show()
        widgets.window.close()
        pass

    def modify_complaint(self,widgets):
        data = [i.text.split(":")[1].strip() for i in widgets.parent.children[:2]]
        window = self.window_manager.modify_complaint_window(data[0])
        self.windows.add(window)
        window.show()
        widgets.window.close()
        pass

    def modify_complainer(self,widgets):
        data = [i.text.split(":")[1].strip() for i in widgets.parent.children[:2]]
        window = self.window_manager.modify_complainer_window(data[0])
        self.windows.add(window)
        window.show()
        widgets.window.close()
        pass


    def delete_user(self,widgets=None):
        data = [i.text.split(":")[1].strip() for i in widgets.parent.children[:2]]

        def _delete(any_,result):

            cmd = f'DELETE From USERS WHERE Username="{data[0]}"'
            self.server.cursor.execute(cmd)
            self.set_user_table()

            # widgets.window.info_dialog(f"Deleted {data[0]}","")
            # self.connection.commit()

        self.main_window.confirm_dialog("CONFIRM",f"Delete User '{data[0]}'",on_result=_delete)
        widgets.window.close()
        return

    def delete_complaint(self,widgets):
        data = [i.text.split(":")[1].strip() for i in widgets.parent.children[:2]]

        def _delete(any_,result):

            cmd = f'DELETE From COMPLAINT_REGISTER WHERE Complaint_id="{data[0]}"'
            self.server.cursor.execute(cmd)
            self.set_complaint_table()

            # widgets.window.info_dialog(f"Deleted {data[0]}","")
            # self.connection.commit()

        self.main_window.confirm_dialog("CONFIRM",f"Delete Complaint '{data[1]}'",on_result=_delete)
        widgets.window.close()
        return

        pass
    def delete_complainer(self,widgets):
        data = [i.text.split(":")[1].strip() for i in widgets.parent.children[:2]]

        def _delete(any_,result):

            cmd = f'DELETE From COMPLAINER_REGISTRATION WHERE Complainer_id="{data[0]}"'
            self.server.cursor.execute(cmd)
            self.set_complainer_table()

            # widgets.window.info_dialog(f"Deleted {data[0]}","")
            # self.connection.commit()

        self.main_window.confirm_dialog("CONFIRM",f"Delete Complainer '{data[1]}'",on_result=_delete)
        widgets.window.close()
        return

        pass


    # def Cursor(self,username="", password="", host="localhost"):
    #     mydb = mysql.connector.connect(
    #       host=host,
    #       user='root',
    #       password='007281',
    #       database='zenex_complaint_register'
    #       )
    #     self.connection = mydb
    #     self.cursor = self.connection.cursor()

    # def on_exit(self):
    #     self.cursor.close()
    #     self.connection.close()
    #     print('connection closed')


Login("App",'support.it').main_loop()