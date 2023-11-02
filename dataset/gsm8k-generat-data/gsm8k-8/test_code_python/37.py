def solution():
    # Calculate total cost of the order
    hamburgers_cost = 5 * 3
    fries_cost = 4 * 1.2
    soda_cost = 5 * 0.5
    spaghetti_cost = 2.7
    total_cost = hamburgers_cost + fries_cost + soda_cost + spaghetti_cost

    # Calculate cost per person
    num_people = 5
    cost_per_person = total_cost / num_people
    result = cost_per_person
    return result

print(solution())