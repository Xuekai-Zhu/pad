def solution():
    # Calculate the cost of the two tickets from the concert website
    website_tickets_cost = 2 * 50

    # Calculate the cost of the two tickets from the scalper
    scalper_tickets_cost = 2 * 50 * 2.4 - 10

    # Calculate the cost of the discounted ticket
    friend_ticket_cost = 50 * 0.6

    # Calculate the total cost of the tickets
    total_cost = website_tickets_cost + scalper_tickets_cost + friend_ticket_cost * 3
    result = total_cost
    return result

print(solution())