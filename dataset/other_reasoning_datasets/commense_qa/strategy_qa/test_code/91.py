def solution():
    pg_wodehouse_death_year = 1975
    hunger_games_published_year = 2008
    if pg_wodehouse_death_year < hunger_games_published_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())