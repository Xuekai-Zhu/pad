def solution():
    
    original_price = 800
    reduction_percent = 15
    reduction_amount = original_price * (reduction_percent / 100)
    final_price = original_price - reduction_amount
    result = final_price
    return result

print(solution())