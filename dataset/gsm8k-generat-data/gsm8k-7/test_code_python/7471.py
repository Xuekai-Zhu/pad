def solution():
    num_children = 35
    num_chaperones = 5
    num_extra_lunches = 3
    cost_per_lunch = 7

    # Calculate the total number of lunches needed
    total_lunches = num_children + num_chaperones + 1 + num_extra_lunches

    # Calculate the total cost of all lunches
    total_cost = total_lunches * cost_per_lunch
    result = total_cost
    return result

print(solution())