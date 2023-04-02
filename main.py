import pickle
import parser
import sqlite3
import config
import random
import logging
import time
import os
import requests

total_jokes = parser.main()
used = []
if os.path.exists("used.pkl"):
    with open("used.pkl", "rb") as file:
        used = pickle.load(file)
else:
    with open("used.pkl", "wb") as file:
        pickle.dump(used, file)

logging.basicConfig(encoding='utf-8', level=logging.INFO)

class Channel:
    url = "https://api.telegram.org/bot"


    def __init__(self, token, channel_id):
        self.token = token
        self.channel_id = channel_id
        self.method = Channel.url + self.token + "/sendMessage"


    def send_message(self, text: str):
        r = requests.post(self.method, data={"chat_id": self.channel_id, "text": text})

        if r.status_code != 200:
            logging.error("Error!")
        else:
            logging.info("Succesful post in channel.")


def select_anekdot(i: int):
    tele = Channel(config.token, "@anekdotiproshtirlitza")
    db = sqlite3.connect("anekdoti.db")
    cursor = db.cursor()
    cursor.execute("SELECT * from Anekdoti WHERE id=?", (i,))
    logging.info(f"Select {i} joke.")
    tele.send_message(cursor.fetchone()[1])


if __name__ == "__main__":
    for i in range(1, total_jokes + 1):
        with open("used.pkl", "wb") as file:
            pickle.dump(used, file)
        number = random.randint(1, total_jokes + 1)

        if number in used:
            if i > 1:
                i -= 1
            continue

        used.append(number)
        select_anekdot(number)
        time.sleep(10)

