def solution():
    
    initial_bags = 3
    given_away_bags = 2
    additional_bags = 3
    remaining_bags = initial_bags - given_away_bags + additional_bags
    result = remaining_bags
    return result

print(solution())