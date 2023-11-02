def solution():
    
    total_legos_needed = 2 * 240
    legos_remaining = 400 - total_legos_needed
    result = abs(legos_remaining)
    return result

print(solution())