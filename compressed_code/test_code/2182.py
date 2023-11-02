def solution():
    
    spiral_notebook_cost = 15
    personal_planner_cost = 10
    discount = 0.2
    total_cost = (4 * spiral_notebook_cost + 8 * personal_planner_cost) * (1 - discount)
    result = total_cost
    return result

print(solution())