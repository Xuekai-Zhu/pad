def solution():
    johnny_cash_albums_sold = 90_000_000
    population_of_france = 66_000_000
    if johnny_cash_albums_sold >= population_of_france:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())