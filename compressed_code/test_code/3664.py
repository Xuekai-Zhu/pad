def solution():
    
    blue_chairs = 10
    green_chairs = 3 * blue_chairs
    total_blue_green_chairs = blue_chairs + green_chairs
    white_chairs = total_blue_green_chairs - 13
    total_chairs = blue_chairs + green_chairs + white_chairs
    result = total_chairs
    return result

print(solution())