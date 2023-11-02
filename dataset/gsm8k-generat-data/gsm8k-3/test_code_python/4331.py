def solution():
    """Josh has a device that automatically records the temperature in his lab every 5 seconds. To perform an analysis of environmental conditions, Josh lets the device record data for one hour. How many instances of data will the device record?"""
    # Calculate the number of seconds in an hour
    seconds_per_hour = 60 * 60

    # Calculate the number of instances of data recorded in an hour
    instances_of_data = seconds_per_hour / 5

    # Display the number of instances of data recorded
    result = instances_of_data
    return result

print(solution())