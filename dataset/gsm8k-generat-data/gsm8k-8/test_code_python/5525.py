def solution():
    initial_bags = 20
    given_away_bags = 4
    bought_bags = 6

    total_bags = initial_bags - given_away_bags + bought_bags
    result = total_bags
    return result

print(solution())