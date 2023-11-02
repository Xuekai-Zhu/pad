def solution():
    # Calculate the number of points for each team
    team1_points = 2*12 + 1*4  # 2 points for a win, 1 point for a tie
    team2_points = 2*13 + 1*1
    team3_points = 2*8 + 1*10

    # Calculate the total points for all teams
    total_points = team1_points + team2_points + team3_points

    # Calculate the average number of points
    avg_points = total_points / 3

    result = avg_points
    return result

print(solution())