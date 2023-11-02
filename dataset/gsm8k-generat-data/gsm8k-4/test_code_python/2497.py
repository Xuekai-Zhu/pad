def solution():
    """Tim won a $100 raffle. He gave away 20% to his friend. How much did he keep?"""
    # Define the amount won in the raffle
    raffle_winnings = 100

    # Calculate the amount given away to his friend
    friend_share = raffle_winnings * 0.2

    # Calculate the amount Tim kept
    kept_amount = raffle_winnings - friend_share

    result = kept_amount
    return result

print(solution())