import toga
from toga.style.pack import LEFT,RIGHT,TOP,ROW,Pack,BOTTOM,COLUMN,CENTER
from login_back import login

class Login(toga.App):
	def startup(self):
		self.main_window = toga.MainWindow(title="Login")
		box = toga.Box()

		self.user_input = toga.TextInput(placeholder="Username")
		self.pass_input = toga.PasswordInput(placeholder="Password")
		login_button = toga.Button("Log In",on_press=self.verify_user)

		username = toga.Label("Username")
		password = toga.Label("Password")
		self.status = toga.Label("")

		box.add(username)
		box.add(self.user_input)
		box.add(password)
		box.add(self.pass_input)
		box.add(login_button)
		box.add(self.status)

		box.style.update(direction=COLUMN)
		self.user_input.style.update(padding_bottom=20)
		self.pass_input.style.update(padding_bottom=20)
		login_button.style.update(padding_bottom=20)
		self.status.style.update(text_align=CENTER)

		self.main_window.content = box
		self.main_window.show()
	def verify_user(self,widgets):
		user = login(self.user_input.value,self.pass_input.value)
		if(user):
			self.status.text = "User Verified : " +user
		else:
			self.status.text = "Access Denied"


Login('Login','ff.ff.f').main_loop()