def solution():
    """Abraham is buying some toiletries and creates a budget of $60 for his shopping. He buys 4 shower gels for $4 each, a tube of toothpaste for $3, and a box of laundry detergent. If he has $30 remaining in his budget, how much money, in dollars, did Abraham spend on the box of laundry detergent?"""
    # Define the initial budget and the cost of each item
    INITIAL_BUDGET = 60
    SHOWER_GEL_COST = 4
    TOOTHPASTE_COST = 3

    # Calculate the cost of the shower gels and the toothpaste
    shower_gel_total = 4 * SHOWER_GEL_COST
    toothpaste_total = TOOTHPASTE_COST

    # Calculate the amount spent on the shower gels, toothpaste, and laundry detergent
    total_spent = INITIAL_BUDGET - 30
    spent_so_far = shower_gel_total + toothpaste_total
    spent_on_detergent = total_spent - spent_so_far

    # return the result
    result = spent_on_detergent
    return result

print(solution())