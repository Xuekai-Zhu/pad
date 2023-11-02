def solution():
    # Define the number of tanks and pregnant fish per tank
    num_tanks = 3
    pregnant_fish_per_tank = 4

    # Calculate the total number of pregnant fish
    total_pregnant_fish = num_tanks * pregnant_fish_per_tank

    # Calculate the total number of young fish
    young_fish = total_pregnant_fish * 20

    result = young_fish
    return result

print(solution())