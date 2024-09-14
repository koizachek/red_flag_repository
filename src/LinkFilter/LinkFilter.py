class LinkFilter:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def filter_users_with_links(self, followers):
        users_with_links = []
        for follower in followers:
            bio = follower.biography
            if self.analyzer.contains_link(bio):
                users_with_links.append((follower.username, bio))
        return users_with_links
