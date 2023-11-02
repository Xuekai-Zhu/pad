def solution():
    """A spiral notebook costs $15, and a personal planner costs $10. How much would it cost in total to buy 4 spiral notebooks and 8 personal planners at a 20% discount?"""
    # Define the regular prices of the items
    NOTEBOOK_PRICE = 15
    PLANNER_PRICE = 10
    
    # Calculate the discounted prices of the items
    notebook_discount = NOTEBOOK_PRICE * 0.2
    notebook_discounted_price = NOTEBOOK_PRICE - notebook_discount
    
    planner_discount = PLANNER_PRICE * 0.2
    planner_discounted_price = PLANNER_PRICE - planner_discount
    
    # Calculate the total cost of the items with the discount
    total_cost = (notebook_discounted_price * 4) + (planner_discounted_price * 8)
    
    # Display the total cost
    result = total_cost
    return result

print(solution())