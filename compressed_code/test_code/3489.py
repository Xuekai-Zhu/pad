def solution():
    
    skirt_price = 13
    blouse_price = 6
    total_skirt_cost = 2 * skirt_price
    total_blouse_cost = 3 * blouse_price
    total_cost = total_skirt_cost + total_blouse_cost
    change = 100 - total_cost
    result = change
    return result

print(solution())