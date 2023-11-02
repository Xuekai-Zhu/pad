def solution():
    """A spiral notebook costs $15, and a personal planner costs $10. How much would it cost in total to buy 4 spiral notebooks and 8 personal planners at a 20% discount?"""
    spiral_notebook_cost = 15
    personal_planner_cost = 10
    discount = 0.2
    total_cost = (4 * spiral_notebook_cost + 8 * personal_planner_cost) * (1 - discount)
    result = total_cost
    return result

print(solution())