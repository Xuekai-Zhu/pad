def solution():
    """A casino table pays 3:2 if you get a blackjack with your first 2 cards. If you scored a blackjack and were paid $60, what was your original bet?"""
    payout_ratio = 3/2
    payout_amount = 60
    original_bet = payout_amount / payout_ratio
    result = original_bet
    return result

print(solution())