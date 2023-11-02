def solution():
    
    hamburgers = 5
    hamburger_price = 4
    fries_packs = 10
    fries_price = 0.3
    fruit_drinks_cans = 5
    fruit_drink_price = 2
    total_cost = (hamburgers * hamburger_price) + (fries_packs * fries_price) + (fruit_drinks_cans * fruit_drink_price)
    change = 50 - total_cost
    result = change
    return result

print(solution())