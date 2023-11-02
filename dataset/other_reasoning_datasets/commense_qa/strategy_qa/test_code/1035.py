def solution():
    hurricane_season_end = 30 # End of November
    halloween_date = 31 # October 31
    if halloween_date <= hurricane_season_end:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())