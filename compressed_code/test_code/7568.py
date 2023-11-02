def solution():
    
    competition1_wins = 40
    competition2_wins = (5/8) * competition1_wins
    competition3_wins = competition1_wins + competition2_wins
    total_wins = competition1_wins + competition2_wins + competition3_wins
    result = total_wins
    return result

print(solution())