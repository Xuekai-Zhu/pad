def solution():
    # Calculate the total water needed for the pigs
    pig_water = 8 * 3

    # Calculate the total water needed for the horses
    horse_water = 10 * 2 * pig_water

    # Calculate the total water needed for the chickens
    chicken_water = 30

    # Calculate the total water needed
    total_water = pig_water + horse_water + chicken_water

    result = total_water
    return result

print(solution())