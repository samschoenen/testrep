class anime():
    name = "gintama"
    source = "manga"
    story_genre = "Comedy"
    setting_genre = "Science Fiction"
    episodes_per_section = []
    score_per_section = []
    def number_of_episodes(self):
        number = 0.0
        for episodes in self.episodes_per_section:
            number = number + episodes
        return number

    def final_score(self):
        score = 0.0
        for i in range(0, len(self.score_per_section)):
            score = score + self.score_per_section[i] * self.episodes_per_section[i]
        score = score // self.number_of_episodes()
        return score