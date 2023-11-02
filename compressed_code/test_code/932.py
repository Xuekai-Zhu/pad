def solution():
    
    current_average = 26
    remaining_games = 20 - 15
    total_points_needed = 30 * 20
    points_already_scored = current_average * 15
    points_needed = total_points_needed - points_already_scored
    average_needed = points_needed / remaining_games
    result = average_needed
    return result

print(solution())