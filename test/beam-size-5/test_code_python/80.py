def solution():
    
    # Define the number of games played and the number of games won
    games_played = 22
    games_won = games_played + 8

    # Calculate the number of games won by the team
    games_won_by_team = games_won - games_played

    # Display the number of games won by the team
    result = games_won_by_team
    return result

print(solution())