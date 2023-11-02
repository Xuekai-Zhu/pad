def solution():
    """Alice was able to sell $2500 worth of gadgets. For this month, she expects to receive her monthly basic salary of $240 and a 2% commission from these sales. How much is she going to save this month if she usually saves 10% of her total earnings?"""
    # Define the sales amount and commission rate
    sales_amount = 2500
    commission_rate = 0.02

    # Calculate the commission earned
    commission = sales_amount * commission_rate

    # Calculate the total earnings
    total_earnings = commission + 240

    # Calculate the amount saved
    amount_saved = total_earnings * 0.1

    result = amount_saved
    return result

print(solution())