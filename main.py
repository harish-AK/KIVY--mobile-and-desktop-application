import kivy
from kivy.app import App       #base Class of your App inherits from the App class
from kivy.uix.label import Label #The uix module is the section that holds the user interface elements like layouts and widgets.

class MyApp(App): # declare base class of kivy app
  
    def build(self):  # this is the function where we return our root widget-elements of gui
        # Create a label widget with some text
        label = Label(text="my first  Kivy application ")  # labels will be the root widget

        # Return the label widget as the root widget of the app
        return label

if __name__ == '__main__':
    MyApp().run()
