import requests
from bs4 import BeautifulSoup
import sqlite3

urls = [
        "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86", 
        "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86/2", 
        "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86/3", 
        "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86/4"
]
total_jokes = 0

def parse(urls):
    jokes = []

    for url in urls:
        resp = requests.get(url)
        sp = BeautifulSoup(resp.text, "html.parser")
        cleanSp = BeautifulSoup(str(sp).replace("<br/>", '\n'), "html.parser")

        jk = cleanSp.find_all("div", class_="text")
        for joke in jk:
            jokes.append(joke.text)

    return jokes


def main() -> None:
    global total_jokes
    jokes = parse(urls)
    total_jokes = len(jokes)
    db = sqlite3.connect("anekdoti.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS Anekdoti")
    cursor.execute("CREATE TABLE Anekdoti (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)")

    for joke in jokes:
        cursor.execute("INSERT INTO Anekdoti(text) VALUES(?)", (joke,))

    db.commit()
    db.close()


if __name__ == "__main__":
    main()
    print(total_jokes)

