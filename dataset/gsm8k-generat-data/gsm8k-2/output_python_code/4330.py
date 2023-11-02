def solution():
    """Josh has a device that automatically records the temperature in his lab every 5 seconds. To perform an analysis of environmental conditions, Josh lets the device record data for one hour. How many instances of data will the device record?"""
    seconds_per_minute = 60
    minutes_per_hour = 60
    total_seconds = seconds_per_minute * minutes_per_hour
    instances_per_second = 1 / 5
    total_instances = total_seconds * instances_per_second
    result = total_instances
    return result

print(solution())