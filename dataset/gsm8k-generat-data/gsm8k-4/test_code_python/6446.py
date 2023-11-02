def solution():
    """A family bought a 24 pack of bottled water. They drank 1/3 of them on the first day and 1/2 of what was left after the first day on the second day. How many bottles of water remain after 2 days?"""
    # Define the initial number of bottles
    initial_bottles = 24

    # Calculate the number of bottles drank on the first day
    first_day_bottles = initial_bottles // 3

    # Calculate the number of bottles remaining after the first day
    remaining_bottles = initial_bottles - first_day_bottles

    # Calculate the number of bottles drank on the second day
    second_day_bottles = remaining_bottles // 2

    # Calculate the number of bottles remaining after the second day
    remaining_bottles -= second_day_bottles

    # Return the result
    result = remaining_bottles
    return result

print(solution())