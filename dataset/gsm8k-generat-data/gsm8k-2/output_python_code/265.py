def solution():
    """Johns goes to the gym 3 times a week. He spends 1 hour each day lifting weight. Additionally, he also spends a third of his weightlifting time warming up and doing cardio each day. How many hours does he spend at the gym a week?"""
    days_per_week = 3
    lifting_time_per_day = 1
    warmup_time_per_day = lifting_time_per_day / 3
    total_time_per_day = lifting_time_per_day + warmup_time_per_day
    total_time_per_week = total_time_per_day * days_per_week
    result = total_time_per_week
    return result

print(solution())