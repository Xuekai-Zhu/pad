def solution():
    """Carol sells tickets for an exhibition. During three days she sold tickets worth $960. One ticket costs $4. How many tickets on average did she sell during one of these three days?"""
    # Define the total amount of money earned from ticket sales
    total_money = 960

    # Define the cost of one ticket
    ticket_cost = 4

    # Calculate the total number of tickets sold
    total_tickets = total_money / ticket_cost

    # Calculate the average number of tickets sold per day
    avg_tickets_per_day = total_tickets / 3

    # return the result
    result = avg_tickets_per_day
    return result

print(solution())