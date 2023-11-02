def solution():
    
    first_two_rounds = 2 * 6
    last_round = 4
    last_round_wins = last_round / 2
    total_matches_won = first_two_rounds + last_round_wins
    result = total_matches_won
    return result

print(solution())