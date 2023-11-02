def solution():
    # Calculate the total number of chairs in the morning
    red_chairs = 4
    yellow_chairs = 2*red_chairs
    blue_chairs = yellow_chairs - 2
    total_chairs = red_chairs + yellow_chairs + blue_chairs

    # Calculate the number of chairs left in the afternoon after Lisa borrows 3 chairs
    chairs_left = total_chairs - 3
    result = chairs_left
    return result

print(solution())