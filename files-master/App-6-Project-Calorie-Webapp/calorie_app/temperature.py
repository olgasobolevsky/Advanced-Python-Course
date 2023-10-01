import requests
from selectorlib import Extractor


class Temperature:
    """
    Represents a temperature value extracted from the timeanddate.com/weather webpage using xpath
    """
    base_url = 'https://www.timeanddate.com/weather/'
    yaml_file = 'temperature.yaml'
    default_temperature = 24

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        """ Construct url"""
        url = self.base_url + str(self.country).lower() + '/' + str(self.city).lower()
        """ Get the page text"""
        request = requests.get(url)
        text = request.text
        """Extract the temperature object"""
        extractor = Extractor.from_yaml_file(self.yaml_file)
        try:
            raw_result = extractor.extract(text)
            """Extract the number only"""
            result = float(raw_result['temp'].replace("\xa0°C", ""))
        except:
            print("Can't find your location. Using default temperature: 24C")
            result = self.default_temperature
        return result
