def solution():
    
    cheeseburger_price = 3.65
    milkshake_price = 2
    coke_price = 1
    fries_price = 4
    cookie_price = 0.5
    tax = 0.2
    total_price = 2 * cheeseburger_price + milkshake_price + coke_price + fries_price + 3 * cookie_price + tax
    each_pays = total_price / 2
    change = 15 - each_pays
    result = change
    return result

print(solution())