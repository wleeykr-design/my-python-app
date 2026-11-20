from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.text_label = Label(
            text="Welcome! Offline Python App",
            font_size='24sp'
        )
        
        action_button = Button(
            text="Click Me",
            size_hint=(1, 0.3),
            font_size='22sp'
        )
        action_button.bind(on_press=self.on_button_click)
        
        layout.add_widget(self.text_label)
        layout.add_widget(action_button)
        return layout

    def on_button_click(self, instance):
        self.text_label.text = "Success! Working 100% Offline"

if __name__ == '__main__':
    MyApp().run()
