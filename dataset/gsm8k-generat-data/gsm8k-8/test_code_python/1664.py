def solution():
    # Calculate the number of matches in the first 2 rounds
    first_two_rounds_matches = 6 * 2
    
    # Calculate the number of matches in the last round
    last_round_matches = 4
    
    # Calculate the number of matches Brendan won in the last round
    last_round_wins = last_round_matches / 2
    
    # Calculate the total number of wins
    total_wins = first_two_rounds_matches + last_round_wins
    
    result = total_wins
    return result

print(solution())