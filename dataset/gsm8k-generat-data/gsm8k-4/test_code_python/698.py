def solution():
    """On a 16 GB (gigabyte) capacity USB drive, 50% is already busy. Calculate the number of gigabytes still available."""
    # Define the capacity of the USB drive
    usb_capacity = 16

    # Calculate the number of gigabytes already used
    used_capacity = usb_capacity * 0.5

    # Calculate the number of gigabytes still available
    available_capacity = usb_capacity - used_capacity

    # return the result
    result = available_capacity
    return result

print(solution())