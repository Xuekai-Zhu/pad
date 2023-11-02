def solution():
    # Calculate the points for each team
    first_team_points = 2 * 12 + 1 * 4
    second_team_points = 2 * 13 + 1 * 1
    third_team_points = 2 * 8 + 1 * 10

    # Calculate the total points for the playoff teams
    total_points = first_team_points + second_team_points + third_team_points

    # Calculate the average points for the playoff teams
    average_points = total_points / 3
    result = average_points
    return result

print(solution())