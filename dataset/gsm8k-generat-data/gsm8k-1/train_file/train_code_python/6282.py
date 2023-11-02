def solution():
    """James decides to go to prom with Susan. He pays for everything. The tickets cost $100 each. Dinner is $120. He leaves a 30% tip. He also charters a limo for 6 hours that cost $80 per hour. How much did it all cost?"""
    ticket_cost = 100
    dinner_cost = 120
    tip_percent = 30
    limo_cost_per_hour = 80
    limo_hours = 6
    
    total_tickets_cost = ticket_cost * 2
    total_dinner_cost = dinner_cost + (dinner_cost * (tip_percent / 100))
    total_limo_cost = limo_cost_per_hour * limo_hours
    
    total_cost = total_tickets_cost + total_dinner_cost + total_limo_cost
    
    result = total_cost
    return result

print(solution())