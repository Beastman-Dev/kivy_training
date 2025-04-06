from kivy.app import App
from kivy.uix.button import Button


class FunkyButton(Button):
    pass



class LanguageLearnerApp(App):
    def build(self):
        return FunkyButton(
            pos=(100,100),
            size_hint=(None,None),
            size=(200,200)
        )

if __name__ == "__main__":
    LanguageLearnerApp().run()