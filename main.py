from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from plyer import filechooser

class TestLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwars)
        self.btn = button(text="PDF 선택", size_hint_y=0.2)
        self.btn.bind(on_press=self.select_pdf)
        self.label = Label(text="선택된 파일 없음")
        self.add_widget(self.btn)
        self.add_widget(self.label)

    def select_pdf(self, *args):
        filechooser.open_file(filters=["*.pdf"],on_selection=self.on_selected)
    def on_selected(self, selection):
        if selection:
            self.label.text = selection[0]
            print("선택 파일:", selection[0])

class PdfTestApp(App):
    def build(self):
        return TestLayout()

PdfTestApp().run()