def solution():
    
    total_matches = 8
    krishna_wins = total_matches * 3/4
    callum_wins = total_matches - krishna_wins
    callum_points = callum_wins * 10
    result = callum_points
    return result

print(solution())