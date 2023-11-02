def solution():
    # Define John's initial height in inches
    john_height = 66

    # Calculate his height after 3 months of growth
    john_height += 2 * 3

    # Convert his height to feet
    john_height_in_feet = john_height / 12

    result = john_height_in_feet
    return result

print(solution())