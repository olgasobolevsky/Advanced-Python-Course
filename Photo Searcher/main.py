import urllib.request
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import wikipedia

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def get_image_link(self):
        # Get user query from text input
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the first image URL
        try:
            page = wikipedia.page(query, auto_suggest=False)
            image_link = page.images[0]
        except wikipedia.exceptions.DisambiguationError as e:
            page = wikipedia.page(random.choice(e.options), auto_suggest=False)
            image_link = page.images[0]
        return image_link

    def download_image(self):
        # Save the image
        image_path = 'files/image.jpg'
        urllib.request.urlretrieve(self.get_image_link(), image_path)
        return image_path

    def set_image(self):
        # Add image to Image widget
        self.manager.current_screen.ids.img.source = self.download_image()
        self.manager.current_screen.ids.img.reload()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
