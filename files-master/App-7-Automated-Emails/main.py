import datetime
from time import sleep

import yagmail
import pandas
from news import NewsFeed

sender_email = 'olgasob07@gmail.com'
sender_password = 'zfpjcyvilcnyeqvn'


def send_email():
    name = row['name']
    email_to = row['email']
    interest = row['interest']
    today = datetime.date.today().strftime("%Y-%m-%d")
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    news_feed = NewsFeed(interest=interest, from_date=yesterday, to_date=today)
    contents = f'Hi {name} \n Your news feed from {yesterday} to {today}: \n\n {news_feed.get()}'
    email = yagmail.SMTP(user=sender_email, password=sender_password)
    email.send(to=email_to,
               contents=contents,
               subject=f'The news about {interest} for today')


while True:
    if datetime.datetime.now().hour == 16 and datetime.datetime.now().minute == 19:
        df = pandas.read_excel('people.xlsx')
        for index, row in df.iterrows():
            send_email()
    sleep(60)
