import sys

from PySide6.QtWidgets import QApplication

from app.core.config import Config
from app.core.assistant import Assistant
from app.memory.database import Database
from app.ui.main_window import MainWindow


def main():

    config = Config()

    database = Database(
        config.get("database", "path")
    )

    assistant = Assistant(config)

    app = QApplication(sys.argv)

    window = MainWindow(
        assistant,
        database
    )

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
