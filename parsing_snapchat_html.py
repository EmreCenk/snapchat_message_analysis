
from bs4 import BeautifulSoup
from collections import defaultdict
from typing import Dict, List
from utils import message, count_list_of_words, average_message_length


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
                # print(info[0].text, current_person)
                current_message = message(text = info[0].text, date = current_date, username = current_person)
                people[current_person].append(current_message)
        return people

    def get_most_used_words(self, username: str) -> tuple[List[str], Dict[str, int]]:
        """
        :param username: Username of user you want to perform word frequency analysis on
        :return: A tuple where the first element is the list of most used words in descending order. The second element is a
        dictionary that maps words to how many times they are used.
        """
        parsed = s.parse_people()
        counted = count_list_of_words(parsed[username])
        most_used = sorted(counted, key=lambda x: counted[x], reverse=True)

        return most_used, counted

    def word_length_over_time(self, username) -> List[tuple[str, int]]:
        """
        :param username: Username to analyze
        :return: A list where List[i][0] is the ith date and List[i][1] is the ith total words
        """
        parsed = s.parse_people()
        final_list = []
        for message in parsed[username]:
            final_list.append(
                (message.date, len(message.text))
            )

        return final_list

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    from os import environ

    username = environ["SOME_USERNAME_FOR_SNAP_ANALYSIS"]
    s = snap_html_parser("chat_history.html")
    result = s.word_length_over_time(username)
    # for r in result:
    #     print(r[0] + "\t" + str(r[1]))

    a = 0
    for i in result: a+=i[1]
