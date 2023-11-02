def solution():
    # Calculate the total number of wings Kevin eats per minute
    kevin_wings_per_minute = 64 / 8  # Kevin eats 64 wings in 8 minutes

    # Calculate the wings per minute Alan needs to eat to beat Kevin's record
    alan_wings_per_minute = kevin_wings_per_minute + 1  # Alan needs to eat one more wing per minute

    # Calculate the additional wings per minute Alan needs to eat
    additional_wings_per_minute = alan_wings_per_minute - 5

    result = additional_wings_per_minute
    return result

print(solution())