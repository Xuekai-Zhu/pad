def solution():
    num_fish = 4 + 1 + 3 + 2 + 5
    num_small_fish = 3
    num_big_fish = num_fish - num_small_fish
    num_filets_per_fish = 2

    # Calculate the total number of fish filets
    total_filets = num_big_fish * num_filets_per_fish

    result = total_filets
    return result

print(solution())