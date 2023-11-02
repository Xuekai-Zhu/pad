def solution():
    # Define the original prices
    notebook_price = 15
    planner_price = 10

    # Apply the 20% discount
    notebook_discounted_price = 0.8 * notebook_price
    planner_discounted_price = 0.8 * planner_price

    # Calculate the total cost of 4 notebooks and 8 planners
    total_cost = (4 * notebook_discounted_price) + (8 * planner_discounted_price)
    result = total_cost
    return result

print(solution())