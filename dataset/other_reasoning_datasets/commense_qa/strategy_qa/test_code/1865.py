def solution():
    ratification_year = 1865
    author_death_year = 1888
    if ratification_year < author_death_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())