def solution():
    # Define the total number of fish caught
    total_fish = 36

    # Define the number of fish caught by Carla
    carla_fish = 8

    # Calculate the total number of fish caught by Kyle and Tasha
    kyle_tasha_fish = total_fish - carla_fish

    # Divide the fish caught by Kyle and Tasha evenly
    kyle_fish = kyle_tasha_fish / 2

    result = kyle_fish
    return result

print(solution())