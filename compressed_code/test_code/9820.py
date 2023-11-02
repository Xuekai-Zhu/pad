def solution():
    
    entrance_ticket_revenue = 368
    raffle_revenue = 343
    food_and_drink_revenue = 279
    total_revenue = entrance_ticket_revenue + raffle_revenue + food_and_drink_revenue
    classes = 5
    revenue_per_class = total_revenue / classes
    result = revenue_per_class
    return result

print(solution())