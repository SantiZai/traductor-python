from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from translate import Translator
import speech_recognition as sr

class Ui(ScreenManager):
    pass

class Traductor(MDApp):
    actual = 'en'
    elegido = 'es'
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file('design.kv')
        self.ui = Ui()
        return self.ui
    
    def option_selected(self, option, action):
        option = option.lower()[:2:]
        if action == 'in':
            if option == 'sp': self.actual = 'es'
            else: self.actual = option
        else:
            if option == 'sp': self.elegido = 'es'
            else: self.elegido = option
    
    def change_text(self, input):
        r = sr.Recognizer()
        mic = sr.Microphone()
        translator = Translator(to_lang=self.elegido, from_lang=self.actual)
        if input == 'mic':
            with mic as source:
                audio = r.listen(source)
                salida = r.recognize_google(audio, language=self.actual)
                traducido = translator.translate(salida)
            self.ui.ids.change.text = traducido
        else:
            traducir = self.ui.ids.inp_text.text
            traducido = translator.translate(traducir)
    
if __name__ == '__main__':
    Traductor().run()