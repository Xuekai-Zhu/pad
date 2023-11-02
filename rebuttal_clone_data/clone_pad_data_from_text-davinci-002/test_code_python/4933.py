def solution():
    quarters = 350 / 5
    dimes = quarters * 5
    total = quarters + dimes
    set_aside = total * 0.4
    remaining = total - set_aside
    result = remaining
    
    return result

print(solution())