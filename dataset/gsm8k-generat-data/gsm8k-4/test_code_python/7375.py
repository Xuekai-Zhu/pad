def solution():
    """Carlos is doing his laundry. He needs to wash two loads, which takes 45 minutes per load. Then he can combine both loads and dry them, which takes 75 minutes. How long does his laundry take in total?"""
    # Define the time it takes to wash one load of laundry
    wash_time = 45

    # Define the time it takes to dry the laundry
    dry_time = 75

    # Calculate the total time to wash and dry two separate loads
    separate_time = wash_time * 2 + dry_time * 2

    # Calculate the total time to wash and dry both loads together
    combined_time = wash_time * 2 + dry_time

    # Choose the faster option and calculate the total time
    if separate_time < combined_time:
        total_time = separate_time
    else:
        total_time = combined_time

    result = total_time
    return result

print(solution())