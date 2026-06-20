import sqlite3


class Database:


    def __init__(self,path):

        self.conn = sqlite3.connect(path)

        self.conn.execute(
        """
        CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY,
        role TEXT,
        content TEXT
        )
        """
        )

        self.conn.commit()


    def save_message(
        self,
        role,
        content
    ):

        self.conn.execute(
        """
        INSERT INTO messages(role,content)
        VALUES(?,?)
        """,
        (
            role,
            content
        ))

        self.conn.commit()
