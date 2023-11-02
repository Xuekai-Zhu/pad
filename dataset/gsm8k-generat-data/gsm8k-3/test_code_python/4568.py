def solution():
    """A casino table pays 3:2 if you get a blackjack with your first 2 cards. If you scored a blackjack and were paid $60, what was your original bet?"""
    # Define the payout ratio for a blackjack
    PAYOUT_RATIO = 3/2

    # Calculate the original bet
    original_bet = 60 / PAYOUT_RATIO

    # Display the original bet
    result = original_bet
    return result

print(solution())