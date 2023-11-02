def solution():
    initial_water = 4
    first_drink = initial_water * (1/4)
    second_drink = (initial_water - first_drink) * (2/3)
    remaining_water = initial_water - first_drink - second_drink
    result = remaining_water
    return result

print(solution())