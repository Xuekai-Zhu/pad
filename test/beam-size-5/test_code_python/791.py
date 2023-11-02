def solution():
    
    original_price = 40
    discount = 0.25
    discounted_price = original_price * (1 - discount)
    money_left = discounted_price - 50
    result = money_left
    return result

print(solution())