def solution():
    # Calculate the size of the second tank
    second_tank_size = 48/2  

    # Calculate the number of fish in the first tank
    first_tank_fish = int(48/3) - 1  # Using integer division and subtract 1 for the fish that was eaten

    # Calculate the number of fish in the second tank
    second_tank_fish = int(second_tank_size/2)

    # Calculate the difference in the number of fish between the two tanks
    fish_difference = first_tank_fish - second_tank_fish
    result = fish_difference
    return result

print(solution())