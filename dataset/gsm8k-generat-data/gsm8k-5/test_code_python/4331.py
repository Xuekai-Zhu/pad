def solution():
    seconds_per_minute = 60  # There are 60 seconds in a minute
    minutes_per_hour = 60  # There are 60 minutes in an hour
    seconds_per_hour = seconds_per_minute * minutes_per_hour  # Calculate the total number of seconds in an hour

    data_recorded_every = 5  # The device records data every 5 seconds
    instances_of_data = seconds_per_hour // data_recorded_every  # Calculate the total number of instances of data recorded in one hour

    result = instances_of_data
    return result

print(solution())