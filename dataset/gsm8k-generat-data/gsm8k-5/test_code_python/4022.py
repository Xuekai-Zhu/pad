def solution():
    minutes_per_session = 30  # James meditates for 30 minutes per session
    sessions_per_day = 2  # James meditates twice a day
    minutes_per_week = minutes_per_session * sessions_per_day * 7  # Calculate total minutes per week
    hours_per_week = minutes_per_week / 60  # Convert minutes to hours

    result = hours_per_week
    return result

print(solution())