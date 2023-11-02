def solution():
    initial_time = 35 # watching time before first rewind
    first_rewind_time = 5 # time added by first rewind
    second_watch_time = 45 # watching time before second rewind
    second_rewind_time = 15 # time added by second rewind
    uninterrupted_time = 20 # final uninterrupted watching time

    # Calculate total watching time including rewinds
    total_time = initial_time + first_rewind_time + second_watch_time + second_rewind_time + uninterrupted_time
    result = total_time
    return result

print(solution())