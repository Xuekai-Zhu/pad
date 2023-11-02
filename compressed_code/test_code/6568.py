def solution():
    
    original_price = 20
    discount = 50
    discounted_price = original_price - (original_price * (discount / 100))
    total_price = discounted_price * 4
    result = total_price
    return result

print(solution())