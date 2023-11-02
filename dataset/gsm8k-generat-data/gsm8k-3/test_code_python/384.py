def solution():
    """It takes David 10 minutes to wash 4 windows.  David's house has 64 windows.  How many minutes will it take David to wash all of the windows?"""
    # Determine how many sets of 4 windows David needs to wash
    num_sets = 64 // 4 # Integer division

    # Calculate how long it will take David to wash one set of windows
    set_time = 10

    # Calculate how long it will take David to wash all the windows
    total_time = num_sets * set_time

    # Display the total time it will take
    result = total_time
    return result

print(solution())