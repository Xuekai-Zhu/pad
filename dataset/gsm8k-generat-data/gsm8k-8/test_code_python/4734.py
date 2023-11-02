def solution():
    # Define the number of blue chairs
    blue_chairs = 10

    # Calculate the number of green chairs
    green_chairs = 3 * blue_chairs

    # Calculate the total number of blue and green chairs
    blue_and_green_chairs = blue_chairs + green_chairs

    # Calculate the number of white chairs
    white_chairs = blue_and_green_chairs - 13

    # Calculate the total number of chairs
    total_chairs = blue_chairs + green_chairs + white_chairs
    result = total_chairs
    return result

print(solution())