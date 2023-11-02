def solution():
    """Alice was able to sell $2500 worth of gadgets. For this month, she expects to receive her monthly basic salary of $240 and a 2% commission from these sales. How much is she going to save this month if she usually saves 10% of her total earnings?"""
    # Define the amount of gadgets sold and commission rate
    gadgets_sold = 2500
    commission_rate = 0.02

    # Calculate Alice's commission
    commission = gadgets_sold * commission_rate

    # Calculate Alice's total earnings
    total_earnings = commission + 240

    # Calculate the amount Alice will save
    savings = total_earnings * 0.1

    # Display the amount Alice will save
    result = savings
    return result

print(solution())