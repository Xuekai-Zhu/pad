def solution():
    
    initial_price = 60
    increased_price = initial_price * 1.2
    smaller_price = increased_price * 0.75
    remaining_money = initial_price - smaller_price
    result = remaining_money
    return result

print(solution())