def solution():
    # Calculate the total number of tickets sold
    total_amount = 960
    ticket_price = 4
    total_tickets_sold = total_amount / ticket_price

    # Calculate the average number of tickets sold per day
    number_of_days = 3
    average_tickets_per_day = total_tickets_sold / number_of_days
    result = average_tickets_per_day
    return result

print(solution())