def solution():
    # Define the capacity of the USB drive in gigabytes
    capacity = 16

    # Calculate the amount of gigabytes that are already in use
    used = capacity * 0.5

    # Calculate the amount of gigabytes that are still available
    available = capacity - used
    result = available
    return result

print(solution())