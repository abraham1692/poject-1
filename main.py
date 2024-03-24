import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window  # Import Window module
from kivy.utils import get_color_from_hex  # Import function to get color from hexadecimal value
import random

def mut():
    n1 = random.randint(2,12)
    n2 = random.randint(2,12)
    lis = [n1*n2-1,(n1+3)*n2,n1*n2,abs(int((n1+5)*n2/random.randint(2,10)))]
    random.shuffle(lis)
    dic = {"numeros":(n1,n2),
           "lista":lis,
           "respuesta": n1*n2

    }
    return dic

def dic_num():
    lista = []
    for n in range(10):
        num=mut()
        lista.append(num)
    return lista


class MultiplicacionesApp(App):
    def build(self):
        # Set window size
        Window.size = (420, 720)

        self.lista = dic_num()
        self.current_question = 0
        self.score = 0
        self.attempts = 0

        # Set background color of the window to green
        Window.clearcolor = get_color_from_hex("#49FE9B")

        self.layout = BoxLayout(orientation='vertical')
        
        self.qs_label = Label(text='', font_size='20sp', size_hint_y=None, height=100,color=get_color_from_hex("#C13AF1"))
        self.layout.add_widget(self.qs_label)

        self.choice_btns = []
        # Set button color to blue
        button_color = get_color_from_hex("#1FC3FB")
        font_color = get_color_from_hex("#C13AF1")
        for i in range(4):
            button = Button(text='', font_size='18sp', size_hint_y=None, height=85, background_color=button_color,color=font_color)  # Reduced height by 15 pixels
            button.bind(on_release=lambda btn: self.check_answer(btn))
            self.choice_btns.append(button)
            self.layout.add_widget(button)

        self.feedback_label = Label(text='', font_size='20sp', size_hint_y=None, height=100)
        self.layout.add_widget(self.feedback_label)

        self.score_label = Label(text=f'Score: {self.score}/{len(self.lista)}', font_size='20sp', size_hint_y=None, height=100,color=get_color_from_hex("#C13AF1"))
        self.layout.add_widget(self.score_label)

        self.restart_btn = Button(text='Restart', font_size='20sp', size_hint_y=None, height=100, background_color=button_color,color=font_color)
        self.restart_btn.bind(on_release=lambda btn: self.restart())
        self.layout.add_widget(self.restart_btn)
        self.restart_btn.disabled = True

        self.show_question()

        return self.layout

    def show_question(self):
        if self.current_question < len(self.lista):
            question = self.lista[self.current_question]
            self.qs_label.text = f'¿Cuál es la multiplicación de {question["numeros"][0]} x {question["numeros"][1]}?'
            
            choices = question['lista']
            for i, button in enumerate(self.choice_btns):
                button.text = str(choices[i])

            self.feedback_label.text = ''
        else:
            if self.attempts >= 10:
                self.restart_btn.disabled = False

    def check_answer(self, button):
        if self.current_question < len(self.lista):
            question = self.lista[self.current_question]
            selected_choice = button.text

            self.attempts += 1

            if int(selected_choice) == question['respuesta']:
                self.score += 1
                self.feedback_label.text = 'Correcto!'
            else:
                self.feedback_label.text = 'Incorrecto!'

            self.score_label.text = f'Score: {self.score}/{len(self.lista)}'
            self.current_question += 1
            self.show_question()

    def restart(self, *args):
        self.current_question = 0
        self.score = 0
        self.attempts = 0
        self.score_label.text = f'Score: {self.score}/{len(self.lista)}'
        self.restart_btn.disabled = True
        self.show_question()

if __name__ == '__main__':
    MultiplicacionesApp().run()
