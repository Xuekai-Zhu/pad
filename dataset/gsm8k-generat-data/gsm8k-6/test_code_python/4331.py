def solution():
    # Calculate the number of seconds in one hour
    seconds_in_hour = 60 * 60

    # Calculate the number of instances of data recorded
    instances_of_data = seconds_in_hour / 5  # the device records data every 5 seconds
    result = instances_of_data
    return result

print(solution())