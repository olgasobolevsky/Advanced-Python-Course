import urllib
import webbrowser

from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from filesharer import FileSharer
import time

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """ Starts camera and changes the button text"""
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """ Stops the camera and changes the button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """ Capture the image and saves it in file with date in the filename"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        filepath = f'files/{current_time}.png'
        self.ids.camera.export_to_png(filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.image.source = filepath


class ImageScreen(Screen):
    empty_link_message = 'Create a Link First'

    def create_link(self, filepath):
        """ Creates shareable link to the image file and shows it in the label"""
        file_sharer = FileSharer(filepath=filepath)
        self.ids.shareable_link.text = file_sharer.share()

    def copy_link(self):
        """ Adds shareable link to clipboard"""
        if self.ids.shareable_link.text == '':
            self.show_error(self.empty_link_message)
        else:
            Clipboard.copy(self.ids.shareable_link.text)

    def open_link(self):
        """ Opens shareable link in browser"""
        if self.ids.shareable_link.text == '':
            self.show_error(self.empty_link_message)
        else:
            webbrowser.open(self.ids.shareable_link.text)

    def show_error(self, message):
        """ Shows error message in the label"""
        self.ids.shareable_link.text = message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
