def solution():
    # Calculate the number of fish caught by Kyle and Tasha combined
    k_t_fish = 36 - 8  # Carla caught 8 fish, so Kyle and Tasha caught the remaining fish
    k_fish = k_t_fish / 2  # Kyle and Tasha caught the same number of fish, so divide by 2 to find how many Kyle caught
    result = k_fish
    return result

print(solution())