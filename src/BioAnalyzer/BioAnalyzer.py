import re

class BioAnalyzer:
    def __init__(self):
        self.onlyfans_pattern = re.compile(r'https?://(www\.)?onlyfans\.com/[^\\s]+')
        self.url_pattern = re.compile(r'https?://[^\\s]+')

    def contains_onlyfans_link(self, bio):
        return self.onlyfans_pattern.search(bio) is not None

    def contains_link(self, bio):
        return self.url_pattern.search(bio) is not None
