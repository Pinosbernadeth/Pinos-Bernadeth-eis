from connector import Connector

class Users:

    def check_user(username, password):
        query = "SELECT * FROM users WHERE username=%s AND password=%s"

        Connector.cursor.execute(query, (username, password))
        result = Connector.cursor.fetchone()

        if result is None:
            return False

        return True