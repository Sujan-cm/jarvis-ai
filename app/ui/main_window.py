from PySide6.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(
        self,
        assistant,
        database
    ):

        super().__init__()

        self.assistant = assistant
        self.database = database

        self.setWindowTitle(
            "Jarvis AI"
        )

        self.resize(
            900,
            600
        )

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        self.input = QLineEdit()

        self.input.returnPressed.connect(
            self.send
        )


        layout = QVBoxLayout()

        layout.addWidget(self.chat)
        layout.addWidget(self.input)


        box = QWidget()
        box.setLayout(layout)

        self.setCentralWidget(box)



    def send(self):

        text = self.input.text()

        if not text:
            return


        self.chat.append(
            "You: " + text
        )

        self.input.clear()


        answer = self.assistant.ask(text)


        self.chat.append(
            "\nJarvis: " + answer + "\n"
        )
