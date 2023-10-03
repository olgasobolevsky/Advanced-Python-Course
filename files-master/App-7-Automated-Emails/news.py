# newsapi API key: 54a6f462723047459ee36cd6d6037956
import requests


class NewsFeed:
    """ Represents string of titles and urls to recent articles of specific interest"""
    base_url = 'https://newsapi.org/v2/everything'
    api_key = '54a6f462723047459ee36cd6d6037956'

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ""
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
        return email_body

    def _build_url(self):
        url = f"{self.base_url}?" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}" \
              f"&apiKey={self.api_key}"
        return url
