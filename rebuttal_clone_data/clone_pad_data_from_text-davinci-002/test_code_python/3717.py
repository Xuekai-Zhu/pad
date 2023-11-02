def solution():
    total_plants = 20
    dug_up_plants = 4
    rate_of_growth = 2
    initial_plants = dug_up_plants / (rate_of_growth**3 - 1)
    result = initial_plants
    return result

print(solution())