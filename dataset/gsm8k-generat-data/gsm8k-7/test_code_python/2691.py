def solution():
    total_fish = 36
    carla_fish = 8

    # Subtract Carla's fish from the total fish caught to get the combined number of fish caught by Kyle and Tasha
    kyle_tasha_fish = total_fish - carla_fish

    # Divide the combined number of fish caught by 2 to get the number of fish caught by Kyle and Tasha each
    kyle_tasha_each = kyle_tasha_fish / 2

    result = kyle_tasha_each
    return result

print(solution())