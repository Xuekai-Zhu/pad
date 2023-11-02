def solution():
    
    egg_cost = 5
    egg_price = 0.2
    eggs_sold = egg_cost / egg_price
    eggs_left = 30 - eggs_sold
    result = eggs_left
    return result

print(solution())