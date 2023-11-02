def solution():
    original_price = 500
    first_reduction = original_price * 0.05
    first_price = original_price - first_reduction
    second_reduction = first_price * 0.04
    final_price = first_price - second_reduction
    
    total_reduction = original_price - final_price
    result = total_reduction
    return result

print(solution())