def solution():
    
    original_price = 1200
    increased_price = original_price * 1.1
    decreased_price = increased_price * 0.85
    final_price_lowered = original_price - decreased_price
    result = final_price_lowered
    return result

print(solution())