def solution():
    first_tank_size = 48
    second_tank_size = first_tank_size / 2
    first_tank_fish_size = 3
    second_tank_fish_size = 2

    # Calculate the number of fish that can fit in the second tank
    second_tank_fish_capacity = second_tank_size // 1

    # Calculate the number of fish that can fit in the first tank
    first_tank_fish_capacity = first_tank_size // first_tank_fish_size
    
    # Calculate the number of fish Gail has in the second tank
    num_second_tank_fish = second_tank_fish_capacity

    # Calculate the number of fish Gail has in the first tank
    num_first_tank_fish = first_tank_fish_capacity

    # One fish in the first tank has been eaten, so subtract one from the total
    num_first_tank_fish -= 1

    # Calculate the difference in the number of fish between the two tanks
    difference = num_first_tank_fish - num_second_tank_fish
    result = difference
    return result

print(solution())