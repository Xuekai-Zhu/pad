def solution():
    """A basketball team played 40 games and won 70% of the games. It still had 10 games to play. How many games can they lose to win 60% of their games?"""
    total_games = 50
    current_wins = total_games * 0.7
    remaining_wins_needed = total_games * 0.6 - current_wins
    remaining_games = 10
    max_losses = remaining_games - remaining_wins_needed
    result = max_losses
    return result

print(solution())