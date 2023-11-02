def solution():
    notebook_cost = 15
    planner_cost = 10
    notebooks = 4
    planners = 8
    discount = 20
    notebook_total = notebook_cost * notebooks
    planner_total = planner_cost * planners
    total_cost = notebook_total + planner_total
    result = total_cost - ((discount / 100) * total_cost)
    return result

print(solution())