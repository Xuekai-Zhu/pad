def solution():
    initial_bags = 3
    given_away_bags = 2
    additional_bags = 3

    # Calculate the total number of bags of chocolates Robie has
    total_bags = initial_bags - given_away_bags + additional_bags

    # Calculate the number of bags of chocolates left
    bags_left = total_bags

    result = bags_left
    return result

print(solution())