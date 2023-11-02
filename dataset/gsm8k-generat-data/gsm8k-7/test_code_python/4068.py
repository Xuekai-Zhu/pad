def solution():
    cheap_time = 6
    expensive_time = 8
    num_friends = 3

    # Calculate the time it takes to pick the cheap handcuffs on all ankles
    cheap_total_time = cheap_time * num_friends

    # Calculate the time it takes to pick the expensive handcuffs on all hands
    expensive_total_time = expensive_time * num_friends

    # Return the total time it takes to free all friends
    result = max(cheap_total_time, expensive_total_time)
    return result

print(solution())