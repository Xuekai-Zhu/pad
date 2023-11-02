def solution():
    
    pants_price = 54
    shirt_price = 33
    total_pants_price = 2 * pants_price
    total_shirt_price = 4 * shirt_price
    total_price = total_pants_price + total_shirt_price
    change = 250 - total_price
    result = change
    return result

print(solution())