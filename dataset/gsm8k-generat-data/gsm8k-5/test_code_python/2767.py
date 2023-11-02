def solution():
    breakfast_time = 20  # Polly spends 20 minutes cooking breakfast every day
    lunch_time = 5  # Polly spends 5 minutes cooking lunch every day
    dinner_time_4_days = 10  # Polly spends 10 minutes cooking dinner for 4 days this week
    dinner_time_other_days = 30  # Polly spends 30 minutes cooking dinner for the remaining days

    # Calculate the total time Polly spends cooking this week
    total_time = (breakfast_time + lunch_time) * 7 + dinner_time_4_days * 4 + dinner_time_other_days * 3
    result = total_time
    return result

print(solution())