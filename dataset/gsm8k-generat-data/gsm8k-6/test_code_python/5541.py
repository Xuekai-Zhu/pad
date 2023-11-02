def solution():
    # Calculate the total cost of tickets for 5 adults and 2 children
    ticket_cost = 76 - 12  # subtract the cost of concessions from the total cost
    ticket_cost -= 2*7  # subtract the cost of children's tickets
    adults = 5
    adult_ticket_cost = ticket_cost / adults  # calculate the cost of each adult's ticket
    result = adult_ticket_cost
    return result

print(solution())