import string

video_games: list[str] = ["V Auto Theft Grand ", "Fortnite",
                          "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
# a
games_len = list(filter(lambda x: len(x) > 8, video_games))
print(games_len)
# b
start_f = list(filter(lambda x: x.lower().startswith('f'), video_games))
print(start_f)
# c
two_words = list(filter(lambda x: len(x.split()) == 2, video_games))
print(two_words)
# d
start_v = list(filter(lambda x: x.lower().startswith('v'), video_games))
print(start_v)
# e
signs = set(string.punctuation)
has_signs = list(filter(lambda x: any(c in signs for c in x) , video_games))
print(has_signs)
# f
years: list[int] = [2013, 2017, 2011, 2011, 2016]
games_years = list(zip(video_games, years))
print(games_years)
# f2
after_2014 = list(filter(lambda x: x[1] > 2014, games_years))
print(after_2014)
print()