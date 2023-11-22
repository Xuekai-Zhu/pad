def solution():
    
    # Define the number of games played and the difference in wins between the two teams
    games_played = 22
    wins_difference = 8

    # Calculate the number of wins by subtracting the number of games played from the number of wins
    wins = games_played - wins_difference

    # Return the result
    result = wins
    return result

print(solution())