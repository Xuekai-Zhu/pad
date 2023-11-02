def solution():
    num_people = 2  # Jamie and Oliver are planning the vacation together
    ticket_cost = 24 * num_people  # The cost of plane tickets for both of them
    hotel_cost = 12 * num_people * 3  # The cost of staying in a hotel for 3 days
    total_cost = ticket_cost + hotel_cost  # The total cost of the vacation
    result = total_cost
    return result

print(solution())