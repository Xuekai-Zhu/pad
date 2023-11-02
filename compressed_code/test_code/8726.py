def solution():
    
    initial_cost = 100000
    daily_cost = initial_cost * 0.01
    ticket_price = 10
    tickets_sold_per_day = 150
    
    daily_profit = (ticket_price * tickets_sold_per_day) - daily_cost
    days_to_break_even = initial_cost / daily_profit
    result = days_to_break_even
    return result

print(solution())