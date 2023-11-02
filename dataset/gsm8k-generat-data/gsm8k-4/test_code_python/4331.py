def solution():
    """Josh has a device that automatically records the temperature in his lab every 5 seconds. To perform an analysis of environmental conditions, Josh lets the device record data for one hour. How many instances of data will the device record?"""
    # Define the number of seconds in an hour
    SECONDS_PER_HOUR = 3600

    # Calculate the number of instances of data that will be recorded
    data_instances = SECONDS_PER_HOUR // 5

    # Return the result
    result = data_instances
    return result

print(solution())