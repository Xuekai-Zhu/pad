def solution():
    
    total_sales = 960
    ticket_price = 4
    tickets_sold = total_sales / ticket_price
    days = 3
    average_tickets_per_day = tickets_sold / days
    result = round(average_tickets_per_day)
    return result

print(solution())