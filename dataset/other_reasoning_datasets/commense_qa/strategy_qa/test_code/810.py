def solution():
    albany_ga_population = 75000
    albany_ny_population = 100000
    if albany_ga_population < albany_ny_population:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())