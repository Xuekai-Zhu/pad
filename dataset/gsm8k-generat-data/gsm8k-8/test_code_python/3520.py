def solution():
    # Calculate the total time spent on all activities in minutes
    total_time = 2*60 + 30 + 3*(30) + 20

    # Calculate the time spent watching the comet in minutes
    comet_time = 20

    # Calculate the percentage of time spent watching the comet
    percent_time = (comet_time / total_time) * 100
    rounded_percent = round(percent_time)

    result = rounded_percent
    return result

print(solution())