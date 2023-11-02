def solution():
    """A basketball team played 40 games and won 70% of the games. It still had 10 games to play. How many games can they lose to win 60% of their games?"""
    # Calculate the number of games the team has won
    games_won = int(0.7*40)

    # Calculate the number of games the team needs to win in the remaining 10 games to reach 60% of their overall games won
    games_needed = int(0.6*(40+10))-games_won

    # Calculate the maximum number of games the team can lose in the remaining 10 games and still achieve their goal
    games_can_lose = 10 - games_needed

    # Display the result
    result = games_can_lose
    return result

print(solution())