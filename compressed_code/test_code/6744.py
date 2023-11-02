def solution():
    
    current_points = 26 * 15
    total_points_needed = 30 * 20
    points_needed_per_game = (total_points_needed - current_points) / (20 - 15)
    result = points_needed_per_game
    return result

print(solution())