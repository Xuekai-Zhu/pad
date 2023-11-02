def solution():
    """Tim won a $100 raffle.  He gave away 20% to his friend.  How much did he keep?"""
    # Define the initial prize amount
    prize = 100

    # Calculate the amount Tim gave away
    giveaway = prize * 0.2

    # Calculate the amount Tim kept
    kept = prize - giveaway

    # Display the amount Tim kept
    result = kept
    return result

print(solution())