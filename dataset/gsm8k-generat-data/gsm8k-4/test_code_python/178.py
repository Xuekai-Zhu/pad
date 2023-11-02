def solution():
    """Simon wanted to buy flowers that his mom could plant for Mother's Day. The garden center was offering 10% off all purchases. He bought 5 pansies at $2.50 each, one hydrangea that cost $12.50 and 5 petunias that cost $1.00 each. If he paid with a $50 bill, how much change would Simon receive back from his purchase?"""
    
    # Define the prices and quantities of the flowers
    pansies_price = 2.5
    pansies_qty = 5
    hydrangea_price = 12.5
    hydrangea_qty = 1
    petunias_price = 1
    petunias_qty = 5
    
    # Calculate the total cost before discount
    total_cost = (pansies_price * pansies_qty) + (hydrangea_price * hydrangea_qty) + (petunias_price * petunias_qty)
    
    # Calculate the discount amount
    discount = total_cost * 0.1
    
    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount
    
    # Calculate the amount of change Simon will receive from his $50 bill
    change = 50 - total_cost_after_discount
    
    result = change
    return result

print(solution())