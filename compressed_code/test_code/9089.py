def solution():
    
    red_chairs = 5
    yellow_chairs = 4 * red_chairs
    blue_chairs = yellow_chairs - 2
    total_chairs = red_chairs + yellow_chairs + blue_chairs
    result = total_chairs
    return result

print(solution())