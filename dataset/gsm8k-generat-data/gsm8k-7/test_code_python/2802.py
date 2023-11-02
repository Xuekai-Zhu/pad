def solution():
    spiral_notebook_price = 15
    personal_planner_price = 10
    num_spiral_notebooks = 4
    num_personal_planners = 8
    discount = 0.2

    # Calculate the total cost before discount
    total_cost_before_discount = (spiral_notebook_price * num_spiral_notebooks) + (personal_planner_price * num_personal_planners)

    # Calculate the amount of discount
    discount_amount = total_cost_before_discount * discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    result = total_cost_after_discount
    return result

print(solution())