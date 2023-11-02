def solution():
    # Define the number of red chairs
    red_chairs = 5

    # Calculate the number of yellow chairs
    yellow_chairs = 4 * red_chairs

    # Calculate the number of blue chairs
    blue_chairs = yellow_chairs - 2

    # Calculate the total number of chairs
    total_chairs = red_chairs + yellow_chairs + blue_chairs
    result = total_chairs
    return result

print(solution())