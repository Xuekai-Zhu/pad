def solution():
    """Jan buys 5 dozen roses. Each rose cost $6. Since he bought so many he only needs to pay 80%. How much did he pay?"""
    
    # First, calculate the total cost of the roses before the discount
    dozen = 12
    roses = 5 * dozen
    cost_per_rose = 6
    total_cost = roses * cost_per_rose
    
    # Calculate the discounted price and return it
    discount_percent = 0.20 # 80% discount
    discounted_price = total_cost * (1 - discount_percent)
    result = discounted_price
    return result

print(solution())