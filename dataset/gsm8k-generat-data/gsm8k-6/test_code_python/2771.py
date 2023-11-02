def solution():
    # Calculate the total number of points Jeff scored in 2 hours
    total_points = (2*60) / 5  # Jeff scores a point every 5 minutes, and plays for 2 hours
    games_won = total_points // 8  # Jeff wins a match when he scores 8 points
    result = games_won
    return result

print(solution())