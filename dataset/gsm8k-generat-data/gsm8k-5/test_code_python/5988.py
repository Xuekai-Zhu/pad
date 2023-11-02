def solution():
    num_tanks = 3  # Mark has 3 tanks for pregnant fish
    num_fish_per_tank = 4  # Each tank has 4 pregnant fish
    num_young_per_fish = 20  # Each fish gives birth to 20 young

    # Calculate the total number of young fish
    total_young = num_tanks * num_fish_per_tank * num_young_per_fish
    result = total_young
    return result

print(solution())