def solution():
    # Define Berry's total pages read so far
    total_pages_read = 43 + 65 + 28 + 0 + 70 + 56

    # Define the number of days Berry has read so far
    days_read_so_far = 6

    # Define Berry's goal for the week
    weekly_goal = 7 * 50

    # Calculate how many pages Berry needs to read on Saturday to reach his goal
    pages_needed_on_saturday = weekly_goal - total_pages_read

    # Calculate how many pages Berry needs to read on average per day for the whole week, including Saturday
    total_days = 7
    average_pages_per_day = (weekly_goal - total_pages_read + pages_needed_on_saturday) / total_days

    result = pages_needed_on_saturday
    return result, average_pages_per_day

print(solution())