def solution():
    year_of_marriage = 1962
    year_of_divorce = 1968
    years_of_marriage = year_of_divorce - year_of_marriage
    if years_of_marriage >= 25:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())