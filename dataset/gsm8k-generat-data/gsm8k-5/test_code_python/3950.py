def solution():
    home_team_wins = 3
    home_team_draws = 4
    home_team_losses = 0
    rival_team_wins = home_team_wins * 2  # Rival team has won twice as many matches as home team did
    rival_team_draws = home_team_draws
    rival_team_losses = home_team_losses
    total_matches = (home_team_wins + rival_team_wins + home_team_draws + rival_team_draws +
                     home_team_losses + rival_team_losses)
    result = total_matches
    return result

print(solution())