def solution():
    """Jack has $45 and 36 euros. If each euro is worth two dollars, how much money does he have total in dollars?"""
    # Define the value of one euro in dollars
    euro_to_dollar = 2

    # Convert the euros to dollars
    euros_in_dollars = 36 * euro_to_dollar

    # Calculate the total amount in dollars
    total_in_dollars = 45 + euros_in_dollars

    # return the result
    result = total_in_dollars
    return result

print(solution())