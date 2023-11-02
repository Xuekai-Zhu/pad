def solution():
    num_marbles_initial = 400
    num_customers = 20
    marbles_per_customer = 15

    # Calculate the total number of marbles sold to all customers
    total_marbles_sold = num_customers * marbles_per_customer

    # Calculate the number of marbles remaining in the store
    num_marbles_remaining = num_marbles_initial - total_marbles_sold
    result = num_marbles_remaining
    return result

print(solution())