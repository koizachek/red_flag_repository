import instaloader

class InstagramDataLoader:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.L = instaloader.Instaloader()

    def load_profile(self):
        profile = instaloader.Profile.from_username(self.L.context, self.profile_name)
        return profile

    def get_followers(self, profile):
        return profile.get_followers()
