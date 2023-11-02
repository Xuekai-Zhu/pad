def solution():
    """Tina is a professional boxer.  She wins her first 10 fights of her career.  She then goes on to win 5 more before losing her first fight, and then doubles her number of wins before losing again.  She then retires.  How many more wins than losses does she have at the end of her career?"""
    # Initialize number of wins and losses
    wins = 10
    losses = 0

    # Add 5 more wins
    wins += 5

    # Lose first fight
    losses += 1

    # Double number of wins
    wins *= 2

    # Lose second fight and retire
    losses += 1

    # Calculate number of wins more than losses
    diff_wins_losses = wins - losses

    # Display result
    result = diff_wins_losses
    return result

print(solution())