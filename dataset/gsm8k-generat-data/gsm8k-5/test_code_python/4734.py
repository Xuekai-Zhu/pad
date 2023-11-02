def solution():
    # Number of blue chairs
    blue_chairs = 10

    # Number of green chairs (3 times the blue chairs)
    green_chairs = 3 * blue_chairs

    # Number of white chairs (13 fewer than the green and blue chairs combined)
    white_chairs = blue_chairs + green_chairs - 13

    # Total number of chairs in the classroom
    total_chairs = blue_chairs + green_chairs + white_chairs
    result = total_chairs
    return result

print(solution())