def solution():
    minutes_per_hour = 60  # There are 60 minutes in an hour
    total_days = 5  # Jeff runs for an hour every weekday
    thursday_time = 40  # Jeff cut his run on Thursday by 20 minutes
    friday_time = 70  # Jeff jogged 10 minutes more on Friday

    # Calculate the total time Jeff ran for that week
    total_time = (total_days - 1) * minutes_per_hour + (minutes_per_hour - thursday_time) + friday_time
    result = total_time
    return result

print(solution())