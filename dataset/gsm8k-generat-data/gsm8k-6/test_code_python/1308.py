def solution():
    # Calculate the total time Jake spent watching the show from Monday to Thursday
    total_time = 12 + 4 + 6 + (total_time / 2) # where total_time includes the time spent on Monday, Tuesday and Wednesday

    # Calculate the time Jake spent watching the show on Friday
    time_on_friday = 52 - total_time
    result = time_on_friday
    return result

print(solution())