def solution():
    
    tea_price = 10
    cheese_price = tea_price / 2
    butter_price = cheese_price * 0.8
    bread_price = butter_price / 2
    total_price = tea_price + cheese_price + butter_price + bread_price
    result = total_price
    return result

print(solution())