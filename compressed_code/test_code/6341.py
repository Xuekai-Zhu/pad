def solution():
    
    left_after_spending = 24
    fraction_spent = 3/7
    fraction_left = 1 - fraction_spent
    original_amount = left_after_spending / fraction_left
    half_original = original_amount / 2
    result = half_original
    
    return result

print(solution())