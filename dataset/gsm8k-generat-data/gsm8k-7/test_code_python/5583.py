def solution():
    team1_wins = 12
    team1_ties = 4
    team2_wins = 13
    team2_ties = 1
    elsa_wins = 8
    elsa_ties = 10

    # Calculate the total points for each team
    team1_points = (team1_wins * 2) + team1_ties
    team2_points = (team2_wins * 2) + team2_ties
    elsa_points = (elsa_wins * 2) + elsa_ties

    # Calculate the total points for all teams
    total_points = team1_points + team2_points + elsa_points

    # Calculate the average points for the playoff teams
    average_points = total_points / 3
    result = average_points
    return result

print(solution())