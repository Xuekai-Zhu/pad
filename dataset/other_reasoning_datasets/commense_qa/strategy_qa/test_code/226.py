def solution():
    who_formation_year = 1964
    ww2_end_year = 1945
    if who_formation_year > ww2_end_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())