def solution():
    # Calculate Tina's total number of fights and wins before first loss
    total_fights_before_loss = 15
    total_wins_before_loss = 10

    # Calculate Tina's number of wins after first loss and before second loss
    wins_after_first_loss = total_wins_before_loss * 2
    fights_after_first_loss = total_fights_before_loss + wins_after_first_loss - total_wins_before_loss

    # Calculate Tina's total number of wins and losses
    total_wins = total_wins_before_loss + wins_after_first_loss
    total_losses = fights_after_first_loss - total_wins

    # Calculate the difference between Tina's wins and losses
    win_loss_difference = total_wins - total_losses
    result = win_loss_difference
    return result

print(solution())