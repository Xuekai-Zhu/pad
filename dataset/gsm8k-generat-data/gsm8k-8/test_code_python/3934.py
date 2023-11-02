def solution():
    # Define the time spent on Monday and Wednesday
    monday_wednesday_time = 1.5 * 2

    # Define the total time spent from Monday to Thursday
    total_time = 5 - monday_wednesday_time

    # Calculate the time spent on Friday
    friday_time = total_time / 2
    result = friday_time
    return result

print(solution())