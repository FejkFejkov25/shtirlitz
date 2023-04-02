import parser
import sqlite3
import config
import datetime
import random
import time
import requests

total_jokes = parser.main()

class Channel:
    url = "https://api.telegram.org/bot"


    def __init__(self, token, channel_id):
        self.token = token
        self.channel_id = channel_id
        self.method = Channel.url + self.token + "/sendMessage"


    def send_message(self, text: str):
        r = requests.post(self.method, data={"chat_id": self.channel_id, "text": text})

        if r.status_code != 200:
            print("Error!")


def select_anekdot(i: int):
    tele = Channel(config.token, "@telescks")
    db = sqlite3.connect("anekdoti.db")
    cursor = db.cursor()
    cursor.execute("SELECT * from Anekdoti WHERE id=?", (i,))
    tele.send_message(cursor.fetchone()[1])


if __name__ == "__main__":
    for i in range(1, 11):
        number = random.randint(1, total_jokes + 1)
        # today = datetime.date.today()
        # magic_number = (today.year - 2020) * 365 + (today.month - 1) * 30 + today.day
        select_anekdot(number)
        time.sleep(10)

