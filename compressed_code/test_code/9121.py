def solution():
    
    starting_matches = 70
    matches_dropped = 10
    matches_eaten_by_dog = matches_dropped * 2
    remaining_matches = starting_matches - matches_dropped - matches_eaten_by_dog
    result = remaining_matches
    return result

print(solution())