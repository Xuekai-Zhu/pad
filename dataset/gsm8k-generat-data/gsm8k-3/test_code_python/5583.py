def solution():
    """Elsa's hockey team just made the playoffs along with two other teams. They make the playoffs by having the top three highest points for their records. Teams get 2 points for a win, 1 point for a tie, and zero points for a loss. The first-place team has 12 wins and 4 ties. The second-place team has 13 wins and 1 tie. Elsa's team has 8 wins and 10 ties. What is the average number of points for the playoff teams?"""
    # Calculate the total number of points for each team
    team1_points = 12*2 + 4*1
    team2_points = 13*2 + 1*1
    team3_points = 8*2 + 10*1

    # Calculate the total number of points for all three teams
    total_points = team1_points + team2_points + team3_points

    # Calculate the average number of points for the playoff teams
    average_points = total_points / 3

    # Display the average number of points
    result = average_points
    return result

print(solution())