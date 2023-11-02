def solution():
    
    ticket_price = 11
    snacks_price = 3
    headphones_price = 16
    total_expenses = ticket_price + snacks_price + headphones_price
    hourly_income = 12
    hourly_wifi_cost = 2
    break_even_time = total_expenses / (hourly_income - hourly_wifi_cost)
    result = break_even_time
    return result

print(solution())