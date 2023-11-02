def solution():
    """Abraham is buying some toiletries and creates a budget of $60 for his shopping. He buys 4 shower gels for $4 each, a tube of toothpaste for $3, and a box of laundry detergent. If he has $30 remaining in his budget, how much money, in dollars, did Abraham spend on the box of laundry detergent?"""
    budget = 60
    shower_gel_price = 4
    tube_of_toothpaste_price = 3
    remaining_budget = 30
    
    # Calculate total spent on shower gels
    num_shower_gels = 4
    total_shower_gel_cost = num_shower_gels * shower_gel_price
    
    # Calculate total spent on toothpaste
    total_toothpaste_cost = tube_of_toothpaste_price
    
    # Calculate total spent on laundry detergent
    total_laundry_detergent_cost = budget - remaining_budget - total_shower_gel_cost - total_toothpaste_cost
    
    result = total_laundry_detergent_cost
    return result

print(solution())