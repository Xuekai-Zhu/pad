def solution():
    # Calculate the number of wings Kevin eats per minute
    kevin_wings_per_minute = 64 / 8

    # Calculate how many more wings Alan needs to eat per minute to beat Kevin's record
    alan_wings_per_minute_needed = kevin_wings_per_minute + 1 - 5

    result = alan_wings_per_minute_needed
    return result

print(solution())