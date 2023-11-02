def solution():
    """A casino table pays 3:2 if you get a blackjack with your first 2 cards. If you scored a blackjack and were paid $60, what was your original bet?"""
    # Define the payout ratio for getting a blackjack
    payout_ratio = 3/2

    # Calculate the original bet based on the payout and the amount paid
    original_bet = 60 / payout_ratio

    result = original_bet
    return result

print(solution())