def solution():
    total_games_year1 = 20
    total_games_year2 = 20
    percent_attended_year1 = 90
    percent_attended_year2 = percent_attended_year1 - 4
    games_attended_year1 = total_games_year1 * (percent_attended_year1 / 100)
    games_attended_year2 = total_games_year2 * (percent_attended_year2 / 100)
    result = games_attended_year2
    
    return result

print(solution())