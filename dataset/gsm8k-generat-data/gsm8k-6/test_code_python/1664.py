def solution():
    # Calculate the total number of matches Brendan won
    first_round = 6 * 2  # Brendan won all 6 matches in the first 2 rounds
    last_round = 4 / 2  # Brendan won half of the 4 matches in the last round
    total_matches = first_round + last_round
    result = total_matches
    return result

print(solution())