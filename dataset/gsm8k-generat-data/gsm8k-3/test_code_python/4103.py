def solution():
    """Abraham is buying some toiletries and creates a budget of $60 for his shopping. He buys 4 shower gels for $4 each, a tube of toothpaste for $3, and a box of laundry detergent. If he has $30 remaining in his budget, how much money, in dollars, did Abraham spend on the box of laundry detergent?"""
    # Define the cost of each toiletries
    SHOWER_GEL_COST = 4
    TOOTHPASTE_COST = 3

    # Calculate the total cost of the shower gels
    shower_gel_cost = 4 * SHOWER_GEL_COST

    # Calculate the total cost of the toothpaste
    toothpaste_cost = TOOTHPASTE_COST

    # Calculate the total money spent on shower gel and toothpaste
    total_spent = shower_gel_cost + toothpaste_cost

    # Calculate the remaining budget
    remaining_budget = 30

    # Calculate the cost of the laundry detergent
    laundry_detergent_cost = 60 - total_spent - remaining_budget

    # Display the cost of laundry detergent
    result = laundry_detergent_cost
    return result

print(solution())