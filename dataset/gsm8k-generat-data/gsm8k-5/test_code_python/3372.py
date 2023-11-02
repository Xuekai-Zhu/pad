def solution():
    first_10_wins = 10  # Tina wins her first 10 fights
    next_5_wins = 5  # Tina wins 5 more fights before losing
    first_loss = 1  # Tina's first loss is after the 15th fight
    first_half_wins = next_5_wins * 2  # Tina doubles her wins before losing again
    second_loss = 1  # Tina's career ends after her second loss

    # Calculate the total number of wins and losses
    total_wins = first_10_wins + next_5_wins + first_half_wins
    total_losses = first_loss + second_loss

    # Calculate the difference between wins and losses
    difference = total_wins - total_losses
    result = difference
    return result

print(solution())