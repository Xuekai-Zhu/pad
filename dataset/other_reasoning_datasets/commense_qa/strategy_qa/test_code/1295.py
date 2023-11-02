def solution():
    sesame_street_start_year = 1969
    elmo_first_appeared_year = 1980
    if elmo_first_appeared_year > sesame_street_start_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())