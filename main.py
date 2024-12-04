# gui app created for change title of twitter from x or nitter to twitter
# cerated by (snom)

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import webbrowser as wb

class SayHello(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # label widget
        self.greeting = Label(
                        text= "???",
                        font_size= 20,
                        color= 'white'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.3)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.xbutton = Button(
                      text= "__X__",
                      size_hint= (1,0.1),
                      bold= True,
                      background_color ='gray',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.xbutton.bind(on_press=self.xcallback)
        self.window.add_widget(self.xbutton)

        self.nitterbutton = Button(
                      text= "nitter",
                      size_hint= (1,0.1),
                      bold= True,
                      background_color ='gray',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.nitterbutton.bind(on_press=self.nittercallback)
        self.window.add_widget(self.nitterbutton)

        return self.window

    def xcallback(self, instance):
        # multiplay items and open browser
        self.greeting.text = self.user.text[9:]
        wb.open_new_tab(f"https://x{self.greeting.text}")
    def nittercallback(self, instance):
        # multiplay items and open browser
        self.greeting.text = self.user.text[9:]
        wb.open_new_tab(f"https://xcancel{self.greeting.text}")       


if __name__ == "__main__":
    SayHello().run()
