def solution():
    # Calculate the cost of the shampoo and conditioner
    shampoo_cost = 10
    conditioner_cost = 10
    shampoo_and_conditioner_cost = shampoo_cost + conditioner_cost

    # Calculate the cost of the lotion
    lotion_cost = 6
    num_lotions = 3
    lotion_total_cost = lotion_cost * num_lotions

    # Calculate the total cost of the order
    total_cost = shampoo_and_conditioner_cost + lotion_total_cost

    # Calculate how much more money Jackie needs to spend to be eligible for free shipping
    difference = 50 - total_cost
    result = difference
    return result

print(solution())