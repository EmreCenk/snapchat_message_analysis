
from bs4 import BeautifulSoup
from collections import defaultdict
from typing import Dict, List
class message:
    def __init__(self, text: str, date: str, username: str):
        self.text = text
        self.date = date
        self.username = username
    def __repr__(self):
        return self.text
class snap_html_parser(BeautifulSoup):

    def __init__(self, path_to_html: str, **kwargs):
        self.path = path_to_html
        self.chat_text = self.get_html_as_text()
        super().__init__(self.chat_text, "html.parser", **kwargs)


    def get_html_as_text(self) -> str:
        with open(self.path, "r", encoding="utf-8") as file:
            text = file.read()
        return text

    def parse_people(self) -> defaultdict[str, List[message]]:
        people = defaultdict(list)

        current_person = ""
        current_type = ""
        current_date = ""
        for tag in self.find_all("tr"):
            info = tag.find_all("td")
            if len(info) == 3:
                current_person, current_type, current_date = info[0].text, info[1].text, info[2].text

            elif len(info)>0:
                print(info[0].text, current_person)
                current_message = message(text = info[0].text, date = current_date, username = current_person)
                people[current_person].append(current_message)
        return people
if __name__ == '__main__':
    s = snap_html_parser("chat_history.html")
    s.parse_people()


