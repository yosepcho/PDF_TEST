from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from smb.SMBConnection import SMBConnection


class TestLayout(BoxLayout):

    def __init__(self, **kwargs):

        super().__init(orientation="vertical", **kwargs)

        self.result = Label(text="대기중")
        self.btn = Button(text="SMB TEST", size_hint_y=0.2)

        self.btn.bind(on_press=self.test_smb)

        self.add_widget(self.btn)
        self.add_widget(self.result)

    def test_smb(self, *args)

        try:

            conn = SMBConnection(
   	      "ldr",
	      "Dustpno1!",
                    "tablet",
    	      "nas",
   	      use_ntlm_v2=True
            )

            connected = conn.connect("10.29.10.40", 445)

            if connected:
                self.result.text = "연결 성공"
            else:
                self.result.text = "연결 실패"
        except Exception as e:
            self.result.text = str(e)

class TestApp(App):
    def build(self):
        return TestLayout()
TestApp().run()