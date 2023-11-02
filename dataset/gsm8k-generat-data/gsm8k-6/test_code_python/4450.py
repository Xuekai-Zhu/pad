def solution():
    # Calculate the cost of the first two tickets
    cost_of_tickets = 50 * 2

    # Calculate the cost of the next two tickets from the scalper
    cost_of_scalper_tickets = 1.4 * cost_of_tickets  # 240% of the normal price
    cost_of_scalper_tickets -= 10  # Jenna gets $10 off the total payment

    # Calculate the cost of the last discounted ticket
    cost_of_discounted_ticket = 0.6 * cost_of_tickets  # 60% of the normal price

    # Calculate the total cost paid by Jenna's friends
    total_cost = cost_of_tickets + cost_of_scalper_tickets + cost_of_discounted_ticket * 2  # two discounted tickets for the other two friends
    result = total_cost
    return result

print(solution())