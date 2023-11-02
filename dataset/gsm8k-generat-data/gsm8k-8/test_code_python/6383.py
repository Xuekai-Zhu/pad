def solution():
    # Define the cost per pound of vegetables and beef
    veggie_cost_per_pound = 2
    beef_cost_per_pound = veggie_cost_per_pound * 3

    # Calculate the total cost of vegetables and beef
    total_veggie_cost = veggie_cost_per_pound * 6
    total_beef_cost = beef_cost_per_pound * 4

    # Calculate the total cost of everything
    total_cost = total_veggie_cost + total_beef_cost
    result = total_cost
    return result

print(solution())