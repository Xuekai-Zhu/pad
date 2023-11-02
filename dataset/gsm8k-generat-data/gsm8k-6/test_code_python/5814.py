def solution():
    # Calculate the total minutes of reading Hillary needs to do on Sunday
    total_time = 60  # 1 hour is 60 minutes
    minutes_read = 16 + 28  # minutes read on Friday and Saturday
    minutes_left = total_time - minutes_read  # minutes left to be read on Sunday
    result = minutes_left
    return result

print(solution())