from typing import List, Dict, Union
class message:
    def __init__(self, text: str, date: str, username: str):
        self.text = text
        self.date = date
        self.username = username
    def __repr__(self):
        return self.text

def replace_all(string: str, phrases_to_replace):
    new_string = ""
    for k in string:
        if k not in phrases_to_replace:
            new_string += k
    return new_string

def count_list_of_words(wordlist: Union[List[str], List[message]], case_sensitive: bool = True) -> Dict[str, int]:
    counted = {}
    for sentence in wordlist:
        if type(sentence) == message: sentence = sentence.text
        if case_sensitive: sentence = sentence.lower()
        sentence = replace_all(sentence, ".,!()!@#$%^&*?`~")
        sentence = sentence.split(" ")
        for word in sentence:
            if word in counted: counted[word] += 1
            else: counted[word] = 1

    return counted

def average_message_length(messageList: List[message]) -> float:
    total = 0
    for m in messageList:
        total += len(m.text)

    return total/len(messageList)