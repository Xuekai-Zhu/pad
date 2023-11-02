def solution():
    
    total_sales = 960
    ticket_price = 4
    total_tickets = total_sales / ticket_price
    avg_tickets_per_day = total_tickets / 3
    result = avg_tickets_per_day
    return result

print(solution())