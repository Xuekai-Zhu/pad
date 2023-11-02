def solution():
    starting_matches = 70
    dropped_matches = 10
    dog_matches = 2 * dropped_matches

    # Calculate the total number of matches lost
    total_lost = dropped_matches + dog_matches

    # Calculate the number of matches Nate has left
    matches_left = starting_matches - total_lost
    result = matches_left
    return result

print(solution())