def solution():
    
    lemon_cost = 10
    sugar_cost = 5
    cup_cost = 3
    total_expenses = lemon_cost + sugar_cost + cup_cost
    cups_sold = 21
    price_per_cup = 4
    total_revenue = cups_sold * price_per_cup
    profit = total_revenue - total_expenses

    result = profit
    return result

print(solution())