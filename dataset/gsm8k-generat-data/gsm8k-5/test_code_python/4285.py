def solution():
    initial_bags = 3  # Robie bought 3 bags of chocolates
    given_away_bags = 2  # Robie gave 2 bags to her siblings
    remaining_bags = initial_bags - given_away_bags  # Robie has some bags of chocolates left

    # She then bought another 3 bags
    total_bags = remaining_bags + 3

    result = total_bags
    return result

print(solution())