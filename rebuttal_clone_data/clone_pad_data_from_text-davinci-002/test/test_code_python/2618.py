def solution():
    initial_cost = 5
    eggs_bought = 30
    price_per_egg = 0.2
    eggs_sold = initial_cost / price_per_egg
    eggs_left = eggs_bought - eggs_sold
    result = eggs_left
    return result

print(solution())