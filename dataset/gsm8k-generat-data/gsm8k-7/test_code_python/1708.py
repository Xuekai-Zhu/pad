def solution():
    team_2pts = 25
    team_3pts = 8
    team_ft = 10
    opp_2pts = team_2pts * 2
    opp_3pts = team_3pts / 2
    opp_ft = team_ft / 2

    # Calculate the total points scored by Mark's team and their opponents
    team_total = (team_2pts * 2) + (team_3pts * 3) + team_ft
    opp_total = (opp_2pts * 2) + (opp_3pts * 3) + opp_ft
    total_points = team_total + opp_total
    result = total_points
    return result

print(solution())