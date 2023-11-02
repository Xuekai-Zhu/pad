def solution():
    servings_per_carton = 15
    cost_per_carton = 4.0
    num_days = 60

    # Calculate the total number of servings of ice cream Cynthia will eat in 60 days
    total_servings = servings_per_carton * num_days

    # Calculate the total cost of all cartons of ice cream
    total_cost = total_servings * cost_per_carton
    result = total_cost
    return result

print(solution())