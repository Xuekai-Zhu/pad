def solution():
    target_average = 50  # Berry wants to read an average of 50 pages per day
    pages_read_so_far = 43 + 65 + 28 + 0 + 70 + 56  # Berry has read this many pages so far
    days_left = 7 - 6  # Berry only has one day left to reach his goal

    # Calculate the target total number of pages Berry needs to read this week
    target_total = target_average * 7

    # Calculate the number of pages Berry needs to read on Saturday to reach his goal
    pages_to_read = target_total - pages_read_so_far
    pages_to_read = max(pages_to_read, 0)  # If he has already met his goal, he doesn't need to read anything on Saturday

    result = pages_to_read
    return result

print(solution())