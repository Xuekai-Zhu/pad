def solution():
    """Carol sells tickets for an exhibition. During three days she sold tickets worth $960. One ticket costs $4. How many tickets on average did she sell during one of these three days?"""
    total_sales = 960
    ticket_price = 4
    total_tickets = total_sales / ticket_price
    avg_tickets_per_day = total_tickets / 3
    result = avg_tickets_per_day
    return result

print(solution())