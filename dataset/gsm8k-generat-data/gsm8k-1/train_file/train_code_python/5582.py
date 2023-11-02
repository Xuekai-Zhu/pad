def solution():
    """Elsa's hockey team just made the playoffs along with two other teams. They make the playoffs by having the top three highest points for their records. Teams get 2 points for a win, 1 point for a tie, and zero points for a loss. The first-place team has 12 wins and 4 ties. The second-place team has 13 wins and 1 tie. Elsa's team has 8 wins and 10 ties. What is the average number of points for the playoff teams?"""
    team1_wins = 12
    team1_ties = 4
    team2_wins = 13
    team2_ties = 1
    team3_wins = 8
    team3_ties = 10

    team1_points = (team1_wins * 2) + (team1_ties * 1)
    team2_points = (team2_wins * 2) + (team2_ties * 1)
    team3_points = (team3_wins * 2) + (team3_ties * 1)

    total_points = team1_points + team2_points + team3_points
    playoff_teams = 3
    average_points = total_points / playoff_teams
    result = average_points
    return result

print(solution())