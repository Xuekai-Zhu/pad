def solution():
    # Calculate the total cost of the tickets including the service fee
    num_tickets = 3  # Sebastian bought tickets for himself and his parents
    ticket_cost = 44  # cost of one ticket
    service_fee = 18  # online transaction service fee
    total_cost = num_tickets * ticket_cost + service_fee
    result = total_cost
    return result

print(solution())