def solution():
    
    latte_cost = 3.75
    croissant_cost = 3.5
    cookie_cost = 1.25
    week_total_cost = (latte_cost + croissant_cost) * 7 + cookie_cost * 5
    remaining_balance = 100 - week_total_cost
    result = remaining_balance
    return result

print(solution())