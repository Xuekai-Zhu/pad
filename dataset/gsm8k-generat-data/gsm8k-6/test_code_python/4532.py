def solution():
    # Calculate the total water consumption of the cows
    cow_water = 40 * 80 # 40 cows drink 80 liters each
    # Calculate the number of sheep on the farm
    num_sheep = 40 * 10 # 10 times the number of cows
    # Calculate the total water consumption of the sheep
    sheep_water = num_sheep * (1/4) * 80 # each sheep drinks 1/4 times as much water as a cow does
    # Calculate the total water consumption in a week
    total_water = (cow_water + sheep_water) * 7 # 7 days in a week
    result = total_water
    return result

print(solution())