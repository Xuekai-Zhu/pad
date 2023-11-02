def solution():
    """James decides to go to prom with Susan. He pays for everything. The tickets cost $100 each. Dinner is $120. He leaves a 30% tip. He also charters a limo for 6 hours that cost $80 per hour. How much did it all cost?"""
    ticket_cost = 100 * 2
    dinner_cost = 120
    tip_percent = 30
    tip_cost = dinner_cost * (tip_percent / 100)
    limo_cost = 80 * 6
    total_cost = ticket_cost + dinner_cost + tip_cost + limo_cost
    result = total_cost
    return result

print(solution())