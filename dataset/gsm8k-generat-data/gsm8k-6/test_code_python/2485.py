def solution():
    # Calculate the total time Carly spends practicing swimming per week
    butterfly_time = 3 * 4  # 3 hours a day, 4 days a week for butterfly stroke
    backstroke_time = 2 * 6  # 2 hours a day, 6 days a week for backstroke
    total_time_per_week = butterfly_time + backstroke_time

    # Calculate the total time Carly spends practicing swimming in a month
    total_time_per_month = total_time_per_week * 4
    result = total_time_per_month
    return result

print(solution())