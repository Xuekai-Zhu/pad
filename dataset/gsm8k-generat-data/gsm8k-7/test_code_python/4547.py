def solution():
    total_sales = 960
    ticket_price = 4
    num_days = 3

    # Calculate the total number of tickets sold during the three days
    total_tickets_sold = total_sales / ticket_price

    # Calculate the average number of tickets sold per day
    avg_tickets_per_day = total_tickets_sold / num_days
    result = avg_tickets_per_day
    return result

print(solution())