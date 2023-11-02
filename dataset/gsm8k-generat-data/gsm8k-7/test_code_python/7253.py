def solution():
    red_chairs = 4
    yellow_chairs = 2 * red_chairs
    blue_chairs = yellow_chairs - 2

    # Calculate the total number of chairs before Lisa borrows 3
    total_chairs = red_chairs + yellow_chairs + blue_chairs

    # Calculate the total number of chairs after Lisa borrows 3
    chairs_left = total_chairs - 3
    result = chairs_left
    return result

print(solution())