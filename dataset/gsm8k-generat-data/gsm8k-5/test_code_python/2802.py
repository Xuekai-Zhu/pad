def solution():
    # Original cost
    notebook_cost = 15
    planner_cost = 10

    # Calculate discounted cost
    notebook_discount = notebook_cost * 0.2
    planner_discount = planner_cost * 0.2
    discounted_notebook_cost = notebook_cost - notebook_discount
    discounted_planner_cost = planner_cost - planner_discount

    # Calculate total cost for 4 notebooks and 8 planners
    total_cost = (discounted_notebook_cost * 4) + (discounted_planner_cost * 8)
    result = total_cost
    return result

print(solution())