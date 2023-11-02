def solution():
    
    total_patrons = 12 + 27
    carts_needed = total_patrons // 3 + (1 if total_patrons % 3 != 0 else 0)
    result = carts_needed
    return result

print(solution())