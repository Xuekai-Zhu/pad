def solution():
    
    pills_per_bottle = 50
    total_pills_used = (2 * 3 * 2) + ((2 / 2) * 3 * 3) + 2
    pills_left = pills_per_bottle - total_pills_used
    result = pills_left
    return result

print(solution())