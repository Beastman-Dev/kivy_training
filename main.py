from kivy.app import App
from kivy.uix.button import Button

class LanguageLearnerApp(App):
    def build(self):
        return Button(
            text="Hello World",
            pos=(50,50),
            size_hint=(0.8,0.8)
            )
    
if __name__ == "__main__":
    LanguageLearnerApp().run()