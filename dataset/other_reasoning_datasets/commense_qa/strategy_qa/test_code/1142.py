def solution():
    ww2_deaths = 56000000
    france_population = 66000000
    if ww2_deaths >= france_population:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())