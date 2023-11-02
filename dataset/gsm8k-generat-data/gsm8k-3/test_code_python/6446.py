def solution():
    """A family bought a 24 pack of bottled water. They drank 1/3 of them on the first day and 1/2 of what was left after the first day on the second day. How many bottles of water remain after 2 days?"""
    # Define the number of bottles of water in the pack
    TOTAL_BOTTLES = 24

    # Calculate the number of bottles of water remaining after the first day
    remaining_after_day_1 = TOTAL_BOTTLES - (TOTAL_BOTTLES * (1/3))

    # Calculate the number of bottles of water remaining after the second day
    remaining_after_day_2 = remaining_after_day_1 - (remaining_after_day_1 * (1/2))

    # Display the number of bottles of water remaining after 2 days
    result = remaining_after_day_2
    return result

print(solution())