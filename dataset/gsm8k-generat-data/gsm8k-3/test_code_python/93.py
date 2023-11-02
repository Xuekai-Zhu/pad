def solution():
    """John orders food for a massive restaurant. He orders 1000 pounds of beef for $8 per pound. He also orders twice
     that much chicken at $3 per pound. How much did everything cost?"""
    # Calculate the cost of the beef
    beef_cost = 1000 * 8

    # Calculate the amount of chicken ordered
    chicken_ordered = 2 * 1000

    # Calculate the cost of the chicken
    chicken_cost = chicken_ordered * 3

    # Calculate the total cost
    total_cost = beef_cost + chicken_cost

    # Return the result
    result = total_cost
    return result

print(solution())