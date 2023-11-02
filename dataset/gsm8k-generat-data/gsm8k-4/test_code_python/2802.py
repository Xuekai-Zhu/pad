def solution():
    """A spiral notebook costs $15, and a personal planner costs $10. How much would it cost in total to buy 4 spiral notebooks and 8 personal planners at a 20% discount?"""
    # Define the prices of the notebook and planner
    notebook_price = 15
    planner_price = 10

    # Calculate the total cost before discount
    total_cost = (4 * notebook_price) + (8 * planner_price)

    # Calculate the discount
    discount = 0.2 * total_cost

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount

    # Return the result
    result = total_cost_after_discount
    return result

print(solution())