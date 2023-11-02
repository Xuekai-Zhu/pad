def solution():
    """John orders food for a massive restaurant. He orders 1000 pounds of beef for $8 per pound. He also orders twice that much chicken at $3 per pound. How much did everything cost?"""
    # Define the cost and quantity of beef
    beef_cost = 8
    beef_qty = 1000

    # Define the cost and quantity of chicken
    chicken_cost = 3
    chicken_qty = beef_qty * 2

    # Calculate the total cost
    total_cost = (beef_cost * beef_qty) + (chicken_cost * chicken_qty)

    result = total_cost
    return result

print(solution())