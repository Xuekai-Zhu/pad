def solution():
    seconds_per_minute = 60
    minutes_per_hour = 60
    seconds_per_hour = seconds_per_minute * minutes_per_hour
    recording_interval = 5
    number_of_recordings = seconds_per_hour / recording_interval
    result = number_of_recordings
    return result

print(solution())