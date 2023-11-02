def solution():
    
    bottle_price = 10
    can_price = 5
    total_bottle_price = bottle_price * 80
    total_recycling_price = 1500
    total_can_price = (total_recycling_price - total_bottle_price) / can_price
    result = total_can_price
    return result

print(solution())