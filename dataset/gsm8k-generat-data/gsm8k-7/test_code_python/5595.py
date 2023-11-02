def solution():
    initial_cost = 1000000
    years = 30
    halving_period = 10

    # Calculate the number of times the cost is halved during Matty's lifetime
    num_halvings = years // halving_period

    # Calculate the final cost of the ticket
    final_cost = initial_cost / (2 ** num_halvings)

    result = final_cost
    return result

print(solution())