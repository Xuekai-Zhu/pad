def solution():
    """Jack has $45 and 36 euros. If each euro is worth two dollars, how much money does he have total in dollars?"""
    # Define the exchange rate of euros to dollars
    EXCHANGE_RATE = 2

    # Convert euros to dollars
    euro_to_dollar = 36 * EXCHANGE_RATE

    # Calculate the total amount in dollars
    total_dollars = 45 + euro_to_dollar

    # Display the total amount in dollars
    result = total_dollars
    return result

print(solution())