def solution():
    initial_amount = 100
    num_dolls = 3
    doll_cost = 1

    # Calculate the total cost of all dolls
    total_doll_cost = num_dolls * doll_cost

    # Calculate the amount of money Amy has left
    remaining_amount = initial_amount - total_doll_cost
    result = remaining_amount
    return result

print(solution())