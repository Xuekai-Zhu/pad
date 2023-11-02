def solution():
    starting_chickens = 400
    disease_death_rate = 0.4
    alive_chickens = starting_chickens * (1 - disease_death_rate)
    died_chickens = starting_chickens * disease_death_rate
    new_chickens = died_chickens * 10
    total_chickens = alive_chickens + new_chickens
    result = total_chickens
    return result

print(solution())