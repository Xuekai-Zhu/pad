def solution():
    # Define the number of red chairs
    red_chairs = 4

    # Calculate the number of yellow chairs
    yellow_chairs = 2 * red_chairs

    # Calculate the number of blue chairs
    blue_chairs = yellow_chairs - 2

    # Calculate the total number of chairs in the morning
    total_chairs = red_chairs + yellow_chairs + blue_chairs

    # Subtract 3 chairs borrowed by Lisa to get the remaining number of chairs
    remaining_chairs = total_chairs - 3

    result = remaining_chairs
    return result

print(solution())