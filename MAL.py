from utils.Anime import anime
import pandas as pd

print("I rate from 0 to 15 instead of out of 10")

scalelist = ["should not exist", "awful", "very bad", "bad", "mid", "barely passable", "some saving aspects", "ok", "good but", "good", "good+", "very good", "great","amazing","magnifique","mastapiece"]
scale = pd.DataFrame(scalelist)
print(scale)
shows = []

Amagi = anime()
Amagi.name = "Amagi Brilliant Park"
Amagi.source = "Light novel"
Amagi.episodes_per_section = [13.0]
Amagi.score_per_section = [11.0]

Assassination_classroom = anime()
Assassination_classroom.name = "Assasination Classroom"
Assassination_classroom.source = "manga"
Assassination_classroom.episodes_per_section = [22.0, 25.0]
Assassination_classroom.score_per_section = [12.0, 13.0]
shows.append(Assassination_classroom)

Clannad = anime()
Clannad.name = "Clannad"
Clannad.source = "Visual novel"
Clannad.episodes_per_section = [23, 1, 1, 23]
Clannad.score_per_section = [11, 10, 11, 14]
Clannad.setting_genre = "School/Work"
Clannad.story_genre = "Romance/Coming of Age"
shows.append(Clannad)

HxH = anime()
HxH.name = "Hunter x Hunter"
HxH.story_genre = "Shounen"
HxH.setting_genre = "Superpower"
HxH.episodes_per_section = [21.0, 5.0, 10.0, 22.0, 17.0, 61.0, 12.0]
HxH.score_per_section = [12.0, 10.0, 12.0, 15.0, 13.0, 15.0, 13.0]
shows.append(HxH)

series = [(Amagi.name, Amagi.story_genre, Amagi.setting_genre, Amagi.source, Amagi.episodes_per_section, Amagi.score_per_section, Amagi.number_of_episodes(), Amagi.final_score())]
for show in shows:
    series.append((show.name, show.story_genre, show.setting_genre, show.source, show.episodes_per_section, show.score_per_section, show.number_of_episodes(), show.final_score()))

dframe = pd.DataFrame(series, columns=['name', 'Story Genre', 'Setting Genre', 'Based on', 'Episode per section', 'Score for each section', 'Episode number', 'Score'])

print(dframe)