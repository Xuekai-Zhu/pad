def solution():
    # Calculate the total number of tickets sold
    total_sales = 960  # Total sales over three days was worth $960
    ticket_price = 4  # The price of one ticket is $4
    total_tickets = total_sales / ticket_price  # Total number of tickets sold

    # Calculate the average number of tickets sold per day
    days = 3  # Carol sold tickets for three days
    avg_tickets_per_day = total_tickets / days

    result = avg_tickets_per_day
    return result

print(solution())