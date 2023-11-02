def solution():
    max_speed = 1000 # in MB/s
    upload_time = (1000/1000) * 2.5 * 3600 # convert hours to seconds
    time_in_fortnight = 14 * 24 * 3600 # convert fortnight to seconds
    if time_in_fortnight >= upload_time:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())