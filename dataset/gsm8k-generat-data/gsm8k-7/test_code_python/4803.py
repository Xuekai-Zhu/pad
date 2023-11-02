def solution():
    num_people = 8
    apple_weight = 2 # pounds
    apple_price_per_pound = 2.0
    pre_made_pie_crust_cost = 2.0
    lemon_cost = 0.5
    butter_cost = 1.5

    # Calculate the total cost of the ingredients
    total_cost = (apple_price_per_pound * apple_weight) + pre_made_pie_crust_cost + lemon_cost + butter_cost

    # Calculate the cost per serving
    cost_per_serving = total_cost / num_people
    result = cost_per_serving
    return result

print(solution())