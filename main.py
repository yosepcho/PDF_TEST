from kivy.app import App
from kivy.uix.label import Label

try:
    from smb.SMBConnection import SMBConnection
    txt = "Import OK"
except Exception as e:
    txt = str(e)

class TestApp(App):
    def build(self):
        return Label(text=txt)
TestApp().run()