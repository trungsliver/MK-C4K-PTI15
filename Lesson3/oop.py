class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def show_info(self):
        print(f"{self.username} - {self.email} - {self.password}")
