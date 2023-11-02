def solution():
    
    starting_matches = 70
    dropped_matches = 10
    dog_matches = 2 * dropped_matches
    remaining_matches = starting_matches - dropped_matches - dog_matches
    result = remaining_matches
    return result

print(solution())