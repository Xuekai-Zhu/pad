def solution():
    
    pizza_price = 12
    fries_price = 0.3
    soda_price = 2
    pizza_sold = 15
    fries_sold = 40
    soda_sold = 25
    total_sales = (pizza_price * pizza_sold) + (fries_price * fries_sold) + (soda_price * soda_sold)
    money_needed = 500
    money_left_to_raise = money_needed - total_sales
    result = money_left_to_raise
    return result

print(solution())