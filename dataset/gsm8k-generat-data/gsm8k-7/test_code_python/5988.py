def solution():
    num_tanks = 3
    num_fish_per_tank = 4
    num_yfish_per_fish = 20

    # Calculate the total number of pregnant fish
    total_pregnant_fish = num_tanks * num_fish_per_tank

    # Calculate the total number of young fish
    total_young_fish = total_pregnant_fish * num_yfish_per_fish
    result = total_young_fish
    return result

print(solution())