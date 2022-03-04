from utils.Anime import anime
shows = []

Amagi = anime()
Amagi.name = "Amagi Brilliant Park"
Amagi.source = "Light novel"
Amagi.episodes_per_section = [13.0]
Amagi.score_per_section = [11.0]
shows.append(Amagi)

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
shows.append(Clannad)

for show in shows:
    print(show.name + "has a score of %d" % show.final_score())