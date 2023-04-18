import requests
from bs4 import BeautifulSoup
import sqlite3

urls1 = [
        "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86", 
        "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86/2", 
        "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86/3", 
        "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86/4"
]
url2 = "https://allanecdots.ru/stirlitz/"


def parse1(urls):
    jokes = []

    for url in urls:
        resp = requests.get(url)
        sp = BeautifulSoup(resp.text, "html.parser")
        cleanSp = BeautifulSoup(str(sp).replace("<br/>", '\n'), "html.parser")

        jk = cleanSp.find_all("div", class_="text")
        for joke in jk:
            jokes.append(joke.text)

    return jokes


def parse2(url):
    jokes = []
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    cs = BeautifulSoup(str(s).replace("<br>", '\n'), "html.parser") 
    j = cs.find_all("p", class_="anekdot_body")
    for joke in j:
        jokes.append(joke.text)

    for i in range(2, 11):
        resp = requests.get(f"{url}{i}")
        sp = BeautifulSoup(resp.text, "html.parser")
        cleanSp = BeautifulSoup(str(sp).replace("<br>", '\n'), "html.parser")

        jk = cleanSp.find_all("p", class_="anekdot_body")
        for joke in jk:
            jokes.append(joke.text)

    return jokes

def main():
    jokes = []
    part1 = parse1(urls1)
    part2 = parse2(url2)
    for i in part1:
        jokes.append(i)
    for i in part2:
        jokes.append(i)

    total_jokes = len(jokes)
    db = sqlite3.connect("anekdoti.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS Anekdoti")
    cursor.execute("CREATE TABLE Anekdoti (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)")

    for joke in jokes:
        cursor.execute("INSERT INTO Anekdoti(text) VALUES(?)", (joke,))

    db.commit()
    db.close()
    return total_jokes


if __name__ == "__main__":
    main()

