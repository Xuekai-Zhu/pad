def solution():
    # Define the initial poem length and the desired poem length
    initial_length = 24
    desired_length = 90

    # Define the number of lines added per month
    lines_added_per_month = 3

    # Calculate the number of months needed to reach the desired length
    months_needed = (desired_length - initial_length) / lines_added_per_month
    result = months_needed
    return result

print(solution())