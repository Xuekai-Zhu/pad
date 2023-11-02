def solution():
    initial_cost = 100000
    daily_cost = initial_cost * 0.01
    ticket_price = 10
    tickets_sold = 150
    daily_revenue = ticket_price * tickets_sold
    days_to_earn_back_money = initial_cost / daily_revenue
    result = days_to_earn_back_money
    
    return result

print(solution())