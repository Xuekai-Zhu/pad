def solution():
    """The epic poem currently contains 24 lines. If a person adds 3 lines to the poem every month, in how many months will the poem contain 90 lines?"""
    # Define the current number of lines and the desired number of lines
    current_lines = 24
    desired_lines = 90

    # Define the number of lines added per month
    lines_added_per_month = 3

    # Calculate the number of months it will take to reach the desired number of lines
    months = (desired_lines - current_lines) / lines_added_per_month

    # Display the number of months
    result = months
    return result

print(solution())