def solution():
    """Grandma wants to order 5 personalized backpacks for each of her grandchildren's first days of school. The backpacks are 20% off of $20.00 and having their names monogrammed on the back pack will cost $12.00 each. How much will the backpacks cost?"""
    # Define the initial backpack cost and the cost of monogramming
    INITIAL_COST = 20
    MONOGRAMMING_COST = 12
    
    # Calculate the discounted backpack cost
    discounted_cost = INITIAL_COST * 0.8
    
    # Calculate the total cost of one personalized backpack
    total_cost = discounted_cost + MONOGRAMMING_COST
    
    # Calculate the total cost of 5 personalized backpacks
    total_cost_5 = total_cost * 5
    
    result = total_cost_5
    return result

print(solution())