def solution():
    """John books 3 nights at a hotel room for $250 a night.  He has a $100 discount.  How much does he pay?"""
    # Define the cost per night and the discount
    COST_PER_NIGHT = 250
    DISCOUNT = 100

    # Calculate the cost before the discount
    cost_before_discount = COST_PER_NIGHT * 3

    # Calculate the final cost after the discount
    final_cost = cost_before_discount - DISCOUNT

    result = final_cost
    return result

print(solution())