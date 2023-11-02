def solution():
    """A machine at the soda factory can usually fill a barrel of soda in 3 minutes. However this morning a leak went unnoticed and it took 5 minutes to fill one barrel. If the leak remains undetected, how much longer will it take to fill 12 barrels of soda than on a normal day when the machine works fine?"""
    # Define the time it takes to fill a barrel on a normal day and with the leak
    NORMAL_TIME = 3
    LEAK_TIME = 5

    # Calculate the time it takes to fill 12 barrels on a normal day
    normal_time_12 = NORMAL_TIME * 12

    # Calculate the time it takes to fill 12 barrels with the leak
    leak_time_12 = LEAK_TIME * 12

    # Calculate the difference in time
    time_difference = leak_time_12 - normal_time_12

    # Display the time difference
    result = time_difference
    return result

print(solution())