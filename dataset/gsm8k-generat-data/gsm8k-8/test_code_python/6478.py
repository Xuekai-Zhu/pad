def solution():
    # Define the initial height
    initial_height = 0

    # Calculate the height after the first week
    height_after_week1 = initial_height + 2

    # Calculate the height after the second week
    height_after_week2 = height_after_week1 + 2 * 2

    # Calculate the height after the third week
    height_after_week3 = height_after_week2 + 4 * 2 * 2

    # Calculate the final height
    final_height = height_after_week3

    result = final_height
    return result

print(solution())