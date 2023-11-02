def solution():
    """Jorge bought 24 tickets for $7 each. For purchasing so many, he is given a discount of 50%. How much, in dollars, did he spend on tickets?"""
    # Define the number of tickets and the original price per ticket
    num_tickets = 24
    original_price = 7

    # Calculate the total cost before discount
    total_cost_before_discount = num_tickets * original_price

    # Calculate the amount of discount
    discount = total_cost_before_discount * 0.5

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount

    # Return the result
    result = total_cost_after_discount
    return result

print(solution())