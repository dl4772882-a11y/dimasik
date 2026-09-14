from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import webbrowser

class DimasikApp(App):
    def build(self):
        # Это главный контейнер, куда мы складываем все элементы (вертикально)
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Заголовок на экране приложения
        title_label = Label(
            text="Браузер ДИМАСИК", 
            font_size='28sp', 
            bold=True,
            size_hint_y=0.15
        )
        main_layout.add_widget(title_label)
        
        # Поле, куда ты будешь вводить адрес сайта
        self.url_input = TextInput(
            text="https://", 
            multiline=False, 
            font_size='18sp',
            size_hint_y=0.15
        )
        main_layout.add_widget(self.url_input)
        
        # Кнопка для перехода на указанный сайт
        go_button = Button(
            text="Открыть сайт", 
            font_size='20sp',
            bold=True,
            size_hint_y=0.2
        )
        # Говорим кнопке: "При нажатии запусти функцию open_website"
        go_button.bind(on_press=self.open_website)
        main_layout.add_widget(go_button)
        
        # Твоя подпись внизу экрана
        footer_label = Label(
            text="Создано Дмитрием через Python", 
            font_size='14sp',
            size_hint_y=0.5,
            valign='bottom'
        )
        main_layout.add_widget(footer_label)
        
        return main_layout

    def open_website(self, instance):
        # Эта функция берет текст из поля ввода и открывает его в браузере телефона
        url = self.url_input.text
        if url:
            webbrowser.open(url)

if __name__ == '__main__':
    DimasikApp().run()

