def solution():
    """Simon wanted to buy flowers that his mom could plant for Mother's Day. The garden center was offering 10% off all purchases.
    He bought 5 pansies at $2.50 each, one hydrangea that cost $12.50 and 5 petunias that cost $1.00 each.
    If he paid with a $50 bill, how much change would Simon receive back from his purchase?"""
    
    # Calculate total cost before discount
    pansies_cost = 5 * 2.5
    hydrangea_cost = 12.5
    petunias_cost = 5 * 1
    total_cost = pansies_cost + hydrangea_cost + petunias_cost
    
    # Calculate discount and total cost after discount
    discount = total_cost * 0.1
    total_cost_discounted = total_cost - discount
    
    # Calculate change from $50 bill
    change = 50 - total_cost_discounted
    result = change
    
    return result

print(solution())