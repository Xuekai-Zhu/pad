def solution():
    num_knives = 9
    cost_first_knife = 5.0
    cost_next_three = 4.0
    cost_after_three = 3.0

    # Calculate the total cost for the first knife
    total_cost = cost_first_knife

    # Calculate the total cost for the next three knives
    if num_knives > 1:
        total_cost += cost_next_three * min(3, num_knives - 1)

    # Calculate the total cost for the rest of the knives
    if num_knives > 4:
        total_cost += cost_after_three * (num_knives - 4)

    result = total_cost
    return result

print(solution())