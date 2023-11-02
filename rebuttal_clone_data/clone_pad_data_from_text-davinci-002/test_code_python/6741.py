def solution():
    seasons = 12
    episodes_per_season = 20
    episodes_watched = (1/3) * (seasons * episodes_per_season)
    episodes_remaining = seasons * episodes_per_season - episodes_watched
    result = episodes_remaining
    return result

print(solution())