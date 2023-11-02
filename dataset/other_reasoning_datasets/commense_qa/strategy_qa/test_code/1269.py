def solution():
    snow_white_dwarfs = 7
    wonders_players_range = range(2, 8)
    if snow_white_dwarfs in wonders_players_range:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())