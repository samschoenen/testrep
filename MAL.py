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

AoT = anime()
AoT.name = "Attack on Titan"
AoT.story_genre = "epic"
AoT.setting_genre = "Fantasy"
AoT.episodes_per_section = [25, 12, 12, 10, 16, 12]
AoT.score_per_section = [12, 13, 14, 15, 15, 15]
shows.append(AoT)

FZ = anime()
FZ.name = "Fate Zero"
FZ.story_genre = "Tragedy"
FZ.episodes_per_section = [14, 12]
FZ.score_per_section = [14.0, 15.0]
shows.append(FZ)

Fate = anime()
Fate.name = "Fate"
Fate.story_genre = "Action"
Fate.episodes_per_section = [25, 10, 3, 2, 1, 4, 4, 4, 14, 13, 14, 12]
Fate.score_per_section = [7.0, 3, 3, 1, 5, 12, 13, 12, 12, 12, 14, 15]
shows.append(Fate)

Railgun = anime()
Railgun.name = "A Certain Scientific Railgun"
Railgun.story_genre = "Action"
Railgun.setting_genre = "Science Fiction"
Railgun.episodes_per_section = [13, 11, 16, 8, 17, 8]
Railgun.score_per_section = [13, 11, 15, 13, 14, 13]
shows.append(Railgun)

MagicalIndex = anime()

Toaru = anime()

MiA = anime()
MiA.name = "Made in Abyss"
MiA.story_genre = "Adventure"
MiA.setting_genre = "Fantasy"
MiA.episodes_per_section = [14, 4]
MiA.score_per_section = [14, 15]
shows.append(MiA)

CodeGeass = anime()
CodeGeass.name = "Code Geass"
CodeGeass.story_genre = "epic"
CodeGeass.setting_genre = "Science Fiction"
CodeGeass.episodes_per_section = [25, 25]
CodeGeass.score_per_section = [15, 15]
shows.append(CodeGeass)

Monogatari = anime()
Monogatari.name = "Monogatari series"
Monogatari.episodes_per_section = [15]
Monogatari.score_per_section = [14]
shows.append(Monogatari)

series = [(Amagi.name, Amagi.story_genre, Amagi.setting_genre, Amagi.source, Amagi.episodes_per_section, Amagi.score_per_section, Amagi.number_of_episodes(), Amagi.final_score())]
for show in shows:
    series.append((show.name, show.story_genre, show.setting_genre, show.source, show.episodes_per_section, show.score_per_section, show.number_of_episodes(), show.final_score()))

dframe = pd.DataFrame(series, columns=['name', 'Story Genre', 'Setting Genre', 'Based on', 'Episode per section', 'Score for each section', 'Episode number', 'Score'])

print(dframe)