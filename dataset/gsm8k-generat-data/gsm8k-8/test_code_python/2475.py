def solution():
    # Calculate the cost of one lollipop
    cost_per_lollipop = 3/12

    # Calculate the number of lollipops to be shared
    lollipops_shared = 12/4

    # Calculate the cost of the lollipops to be shared
    shared_cost = lollipops_shared * cost_per_lollipop

    # Convert the shared cost to cents
    shared_cost_cents = shared_cost * 100

    result = shared_cost_cents
    return result

print(solution())