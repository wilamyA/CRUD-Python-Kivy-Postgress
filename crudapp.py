import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class CRUDApp(BoxLayout):
    name_input = ObjectProperty(None)
    age_input = ObjectProperty(None)
    add_button = ObjectProperty(None)
    delete_button = ObjectProperty(None)
    update_button = ObjectProperty(None)
    read_button = ObjectProperty(None)

    def add_person(self):
        pass

    def delete_person(self):
        pass

    def update_person(self):
        pass

    def read_person(self):
        pass
