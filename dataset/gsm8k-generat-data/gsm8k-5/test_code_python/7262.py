def solution():
    num_tickets = 3  # Sebastian bought tickets for himself and his parents
    ticket_price = 44  # Tickets were $44 each
    service_fee = 18  # There was an $18 service fee for the online transaction

    # Calculate the total cost of the tickets and service fee
    total_cost = (num_tickets * ticket_price) + service_fee
    result = total_cost
    return result

print(solution())