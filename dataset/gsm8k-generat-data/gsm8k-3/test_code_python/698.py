def solution():
    """On a 16 GB (gigabyte) capacity USB drive, 50% is already busy. Calculate the number of gigabytes still available."""
    # Define the total capacity of the USB drive
    TOTAL_CAPACITY = 16

    # Calculate the number of gigabytes already used
    used_capacity = TOTAL_CAPACITY * 0.5

    # Calculate the number of gigabytes still available
    available_capacity = TOTAL_CAPACITY - used_capacity

    # Display the number of gigabytes still available
    result = available_capacity
    return result

print(solution())