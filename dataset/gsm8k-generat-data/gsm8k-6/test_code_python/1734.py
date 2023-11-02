def solution():
    # Calculate the total points scored by the team in 5 games
    wade_points = 20 * 5  # Wade's total points in 5 games
    teammates_points = 40 * 5 * 4  # Each teammate scores 40 points in 4 games (excluding Wade's game)
    total_points = wade_points + teammates_points
    result = total_points
    return result

print(solution())