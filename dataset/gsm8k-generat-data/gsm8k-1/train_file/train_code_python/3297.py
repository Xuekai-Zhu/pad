def solution():
    """Bill has played 200 games of poker and won 63% of them. If he plays 100 more games and loses 43 of them, what is his new win percentage?"""
    total_games = 200 + 100
    total_wins = (200 * 0.63) + (100 * 0.57)
    total_losses = 43
    new_win_percentage = total_wins / (total_games - total_losses) * 100
    result = new_win_percentage
    return result

print(solution())