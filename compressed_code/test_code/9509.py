def solution():
    
    blue_chairs = 10
    green_chairs = blue_chairs * 3
    total_chairs = blue_chairs + green_chairs
    white_chairs = total_chairs - 13
    total_chairs += white_chairs
    result = total_chairs
    return result

print(solution())