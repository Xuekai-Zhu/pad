def solution():
    """Winwin won $50 in a lottery. She paid 20% for the tax and she paid $5 for the processing fee. How much was she able to take home?"""
    # Define the initial winnings amount
    winnings = 50

    # Calculate the tax amount
    tax = winnings * 0.2

    # Subtract the tax and the processing fee from the winnings to get the final amount taken home
    final_amount = winnings - tax - 5

    result = final_amount
    return result

print(solution())