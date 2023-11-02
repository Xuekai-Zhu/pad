def solution():
    # Calculate the total number of tickets sold by Carol during three days
    total_sales = 960  # total sales worth $960
    ticket_price = 4  # one ticket costs $4
    total_tickets_sold = total_sales / ticket_price  # total number of tickets sold
    avg_tickets_per_day = total_tickets_sold / 3  # average tickets sold per day
    result = avg_tickets_per_day
    return result

print(solution())