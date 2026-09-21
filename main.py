from kivy.app import App
from kivy.uix.label import Label

try:
    from smb.SMBConnection import SMBConnection
    conn = SMBConnection(
        "ldr",
        "Dustpno1!",
        "Tablet",
        "10.29.10.40",
        use_ntlm_v2=True
    ) 
    connected = conn.connect("10.29.10.40", 445)
    txt = str(connected)

except Exception as e:
    txt = str(e)



class TestApp(App):
    def build(self):
        return Label(text=txt)
TestApp().run()