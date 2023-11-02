def solution():
    blueberries_in_europe_year = 1930
    treaty_of_versailles_year = 1920
    if blueberries_in_europe_year > treaty_of_versailles_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())