def solution():
    # Calculate the number of hours Rex will have completed after 6 weeks
    hours_completed = 6 * 4  # 4 sessions per week for 6 weeks, each session is 2 hours long
    hours_remaining = 40 - hours_completed  # Calculate the number of hours remaining to reach his goal
    weeks_remaining = hours_remaining // 4  # Calculate the number of weeks remaining to reach his goal, assuming 4 sessions per week
    result = weeks_remaining
    return result

print(solution())