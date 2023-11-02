def solution():
    
    red_chairs = 4
    yellow_chairs = 2 * red_chairs
    blue_chairs = yellow_chairs - 2
    total_chairs = red_chairs + yellow_chairs + blue_chairs
    borrowed_chairs = 3
    chairs_left = total_chairs - borrowed_chairs
    result = chairs_left
    return result

print(solution())