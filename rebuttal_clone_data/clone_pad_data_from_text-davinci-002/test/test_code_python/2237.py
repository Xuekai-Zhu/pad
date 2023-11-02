def solution():
    home_team_wins = 3
    away_team_wins = home_team_wins * 2
    home_team_losses = 0
    away_team_losses = 0
    home_team_draws = 4
    away_team_draws = 4
    total_matches = home_team_wins + away_team_wins + home_team_losses + away_team_losses + home_team_draws + away_team_draws
    result = total_matches
    return result

print(solution())