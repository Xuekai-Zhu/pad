def solution():
    # Calculate the total points scored by the team
    total_points = 20 + 10 + (6 * 10)  # Lefty scores 20 points, Righty scores half as many (10 points), other teammate scores 6 times as much as Righty (60 points)
    num_players = 3  # there are three players on the team
    
    # Calculate the average points per player
    avg_points = total_points / num_players
    result = avg_points
    return result

print(solution())