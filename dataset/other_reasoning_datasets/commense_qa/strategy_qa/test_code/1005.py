def solution():
    aristotle_death_year = 322
    model_parliament_year = 1295
    if aristotle_death_year < model_parliament_year:
        result = "no"
    else:
        result = "not applicable"
    return result

print(solution())