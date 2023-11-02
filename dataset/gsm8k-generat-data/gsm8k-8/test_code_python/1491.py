def solution():
    initial_marbles = 400
    num_customers = 20
    marbles_per_customer = 15

    total_marbles_sold = num_customers * marbles_per_customer
    remaining_marbles = initial_marbles - total_marbles_sold

    result = remaining_marbles
    return result

print(solution())