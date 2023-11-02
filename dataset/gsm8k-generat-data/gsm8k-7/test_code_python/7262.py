def solution():
    num_tickets = 3
    ticket_price = 44
    service_fee = 18

    # Calculate the total cost of all tickets
    total_tickets_cost = num_tickets * ticket_price

    # Calculate the total cost, including the service fee
    total_cost = total_tickets_cost + service_fee
    result = total_cost
    return result

print(solution())