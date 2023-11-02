def solution():
    # Calculate the cost with the discount for each book
    discount_spiral_notebook = 15 * 0.2  # 20% discount on spiral notebook
    discount_personal_planner = 10 * 0.2  # 20% discount on personal planner
    discounted_spiral_notebook = 15 - discount_spiral_notebook
    discounted_personal_planner = 10 - discount_personal_planner

    # Calculate the total cost with the discount for 4 spiral notebooks and 8 personal planners
    total_cost = (4 * discounted_spiral_notebook) + (8 * discounted_personal_planner)
    result = total_cost
    return result

print(solution())