def solution():
    
    rounds_played = 8
    krishna_won = 3/4 * rounds_played
    callum_won = rounds_played - krishna_won
    points_per_round = 10
    callum_points = callum_won * points_per_round
    result = callum_points
    return result

print(solution())