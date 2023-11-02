def solution():

    total_needed = 500
    pizza_sold = 15
    pizza_price = 12
    fries_sold = 40
    fries_price = 0.30
    soda_sold = 25
    soda_price = 2
    
    money_raised = (pizza_sold * pizza_price) + (fries_sold * fries_price) + (soda_sold * soda_price)
    money_needed = total_needed - money_raised
    result = money_needed
    
    return result

print(solution())