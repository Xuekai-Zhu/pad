def solution():
    
    spiral_notebook_cost = 15
    personal_planner_cost = 10
    num_spiral_notebooks = 4
    num_personal_planners = 8
    discount_percent = 20
    total_cost = (spiral_notebook_cost * num_spiral_notebooks) + (personal_planner_cost * num_personal_planners)
    discount_amount = total_cost * (discount_percent / 100)
    total_cost_after_discount = total_cost - discount_amount
    result = total_cost_after_discount
    return result

print(solution())