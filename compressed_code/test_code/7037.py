def solution():
    
    matinee_tickets_sold = 200
    evening_tickets_sold = 300
    threed_tickets_sold = 100
    matinee_ticket_price = 5
    evening_ticket_price = 12
    threed_ticket_price = 20
    total_matinee_sales = matinee_tickets_sold * matinee_ticket_price
    total_evening_sales = evening_tickets_sold * evening_ticket_price
    total_threed_sales = threed_tickets_sold * threed_ticket_price
    total_sales = total_matinee_sales + total_evening_sales + total_threed_sales
    
    result = total_sales
    return result

print(solution())