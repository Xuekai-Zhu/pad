def solution():
    """The epic poem currently contains 24 lines. If a person adds 3 lines to the poem every month, in how many months will the poem contain 90 lines?"""
    # Define the initial number of lines and the number of lines added each month
    initial_lines = 24
    lines_added_per_month = 3

    # Initialize the month counter
    months = 0

    # Increase the number of lines each month until the target is reached
    while initial_lines < 90:
        initial_lines += lines_added_per_month
        months += 1

    # Display the number of months it took to reach the target number of lines
    result = months
    return result

print(solution())