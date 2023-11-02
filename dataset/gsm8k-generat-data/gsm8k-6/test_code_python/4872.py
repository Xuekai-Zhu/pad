def solution():
    # Calculate the total time to braid all dancers' hair
    total_braids = 8 * 5  # each dancer has 5 braids
    total_time = total_braids * 30  # each braid takes 30 seconds
    total_time_in_minutes = total_time / 60  # convert seconds to minutes
    result = total_time_in_minutes
    return result

print(solution())