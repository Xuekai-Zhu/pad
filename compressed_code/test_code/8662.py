def solution():
    
    pizza_price = 12
    fries_price = 0.30
    soda_price = 2
    total_sales = (pizza_price * 15) + (fries_price * 40) + (soda_price * 25)
    goal_amount = 500
    money_needed = goal_amount - total_sales
    result = money_needed
    return result

print(solution())