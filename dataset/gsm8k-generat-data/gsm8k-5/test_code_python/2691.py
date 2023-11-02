def solution():
    total_fish = 36  # Carla, Kyle, and Tasha caught 36 fish
    carla_fish = 8  # Carla caught 8 fish
    remaining_fish = total_fish - carla_fish  # Kyle and Tasha caught the rest of the fish

    # Since Kyle and Tasha caught the same number of fish, we can divide the remaining fish by 2 to get the number caught by each of them
    kyle_tasha_fish = remaining_fish / 2

    result = kyle_tasha_fish
    return result

print(solution())