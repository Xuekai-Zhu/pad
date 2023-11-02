def solution():
    
    total_chairs = 42 + 15
    high_chairs = 8
    regular_chairs = 5 * high_chairs
    remaining_chairs = total_chairs - high_chairs - regular_chairs
    result = remaining_chairs
    return result

print(solution())