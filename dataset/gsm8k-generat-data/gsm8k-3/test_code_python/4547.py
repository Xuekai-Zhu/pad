def solution():
    """Carol sells tickets for an exhibition. During three days she sold tickets worth $960. One ticket costs $4. How many tickets on average did she sell during one of these three days?"""
    # Define the total amount of money earned from selling tickets
    total_earnings = 960

    # Define the price of one ticket
    ticket_price = 4

    # Calculate the total number of tickets sold
    total_tickets = total_earnings / ticket_price

    # Calculate the average number of tickets sold per day
    avg_tickets_per_day = total_tickets / 3

    # Display the average number of tickets sold per day
    result = avg_tickets_per_day
    return result

print(solution())