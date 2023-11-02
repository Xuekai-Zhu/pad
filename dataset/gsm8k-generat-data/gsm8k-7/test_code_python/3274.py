def solution():
    initial_fish = 60
    worm_eats_per_day = 2
    days_without_discovery = 21  # 2 weeks + 1 week
    days_with_discovery = 7  # 1 week

    # Calculate the total number of fish eaten by the worm before discovery
    total_fish_eaten = worm_eats_per_day * days_without_discovery

    # Calculate the remaining number of fish after the worm has eaten
    remaining_fish = initial_fish - total_fish_eaten

    # Add the 8 new fish that James added to the aquarium
    total_fish = remaining_fish + 8
    result = total_fish
    return result

print(solution())