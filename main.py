import requests
from bs4 import BeautifulSoup

urls = ["https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86", "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86/2", "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86/3", "https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86/4"]


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
    jokes = parse(urls)
    with open("anekdoti.txt", "w") as file:
        for joke in jokes:
            file.write(joke)
            file.write('\n' * 4)


if __name__ == "__main__":
    main()

