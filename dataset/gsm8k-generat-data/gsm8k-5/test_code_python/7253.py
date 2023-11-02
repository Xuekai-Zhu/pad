def solution():
    red_chairs = 4
    yellow_chairs = red_chairs * 2
    blue_chairs = yellow_chairs - 2
    total_chairs = red_chairs + yellow_chairs + blue_chairs
    borrowed_chairs = 3
    remaining_chairs = total_chairs - borrowed_chairs
    result = remaining_chairs
    return result

print(solution())