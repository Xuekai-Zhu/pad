def solution():
    average_score = 287
    num_players = 4
    num_rounds = 9
    total_score = 10440
    current_average = total_score / (num_players * num_rounds)
    points_needed = average_score - current_average
    result = points_needed
    
    return result

print(solution())