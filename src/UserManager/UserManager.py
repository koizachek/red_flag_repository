class UserManager:
    def __init__(self):
        self.users_with_links = []

    def add_user(self, username, bio):
        self.users_with_links.append((username, bio))

    def print_users(self):
        for user, bio in self.users_with_links:
            print(f"User: {user}, Bio: {bio}")
