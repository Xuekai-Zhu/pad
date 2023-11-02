def solution():
    
    cart_total = (1.5 * 6) + 3 + 2.50 + (4 * 0.75) + (2 * 2) + 2.50
    min_spend = 35
    diff = min_spend - cart_total
    result = diff if diff > 0 else 0
    return result

print(solution())