from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):  # login class inherit gridlayout class

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Label(text='gender'))
        self.gender=TextInput(multiline=False)
        self.add_widget(self.gender)


class MyApp(App):

    def build(self):
        return LoginScreen()
l=LoginScreen()

if __name__ == '__main__':
    MyApp().run()