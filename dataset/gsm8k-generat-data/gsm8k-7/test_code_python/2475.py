def solution():
    num_lollipops = 12
    total_cost = 3
    shared_fraction = 0.25

    # Calculate the cost of one lollipop
    cost_per_lollipop = total_cost / num_lollipops

    # Calculate the number of lollipops shared
    num_shared_lollipops = num_lollipops * shared_fraction

    # Calculate the cost of the shared lollipops
    shared_cost = num_shared_lollipops * cost_per_lollipop

    # Convert the shared cost to cents
    shared_cost_cents = shared_cost * 100
    result = shared_cost_cents
    return result

print(solution())