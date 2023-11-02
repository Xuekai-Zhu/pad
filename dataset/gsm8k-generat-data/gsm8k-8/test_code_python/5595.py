def solution():
    # Define the initial ticket cost
    ticket_cost = 1000000

    # Determine the number of times the cost has been halved
    num_halvings = 3

    # Halve the cost for each period of 10 years
    for i in range(num_halvings):
        ticket_cost = ticket_cost / 2

    result = ticket_cost
    return result

print(solution())