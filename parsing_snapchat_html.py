


class snap_html_parser:

    def __init__(self, path_to_html: str):
        self.path = path_to_html
    def get_html_as_text(self) -> str:
        with open(self.path, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    def initialize_text(self):
        self.chat_text = self.get_html_as_text()

if __name__ == '__main__':
    s = snap_html_parser("chat_history.html")
    s.get_html_as_text()



