def solution():
    # Calculate the total time Polly spends cooking this week
    breakfast_time = 20 * 7  # 20 minutes every day for a week
    lunch_time = 5 * 7  # 5 minutes every day for a week
    dinner_time = 10 * 4 + 30 * 3  # 10 minutes cooking dinner for 4 days and 30 minutes cooking dinner for 3 days
    total_time = breakfast_time + lunch_time + dinner_time
    result = total_time
    return result

print(solution())