def solution():
    driving_time_per_day = 40  # 20 minutes to and from school each day
    driving_hours_per_day = driving_time_per_day / 60
    required_driving_hours = 50

    # Calculate how many school days it will take to reach the required driving hours
    num_school_days = required_driving_hours / driving_hours_per_day

    result = num_school_days
    return result

print(solution())