def solution():
    # Cost of one ticket
    ticket_cost = 3

    # Number of tickets sold per minute
    tickets_per_minute = 5

    # Total number of tickets sold in 6 minutes
    tickets_sold = 6 * tickets_per_minute

    # Total earnings from tickets in 6 minutes
    total_earnings = tickets_sold * ticket_cost
    result = total_earnings
    return result

print(solution())