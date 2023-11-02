def solution():
    # Define the time spent outlining and writing
    outlining_time = 30
    writing_time = outlining_time + 28

    # Calculate the time spent practicing
    practicing_time = 0.5 * writing_time

    # Calculate the total time spent on the speech
    total_time = outlining_time + writing_time + practicing_time
    result = total_time
    return result

print(solution())