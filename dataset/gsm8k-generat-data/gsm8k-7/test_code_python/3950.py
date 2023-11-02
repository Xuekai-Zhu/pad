def solution():
    home_team_wins = 3
    home_team_draws = 4
    home_team_losses = 0

    # Calculate the number of wins of the rival team
    rival_team_wins = home_team_wins * 2

    # Calculate the total number of matches played by each team
    total_matches_played = (home_team_wins + home_team_draws + home_team_losses) + (
            rival_team_wins + home_team_draws + home_team_losses)

    result = total_matches_played
    return result

print(solution())