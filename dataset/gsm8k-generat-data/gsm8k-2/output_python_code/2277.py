def solution():
    """Johnny is a dog walker. He can walk 3 dogs at once. He gets paid $15 for a 30-minute walk and $20 for a 60-minute walk. Johnny works for 4 hours per day. If he always walks the maximum number of dogs possible and 6 dogs have 60-minute walks per day, how much money does he make in a week where he works 5 days?"""
    max_dogs_per_walk = 3
    short_walk_time = 30
    long_walk_time = 60
    short_walk_pay = 15
    long_walk_pay = 20
    total_work_hours_per_day = 4
    total_work_days_per_week = 5
    daily_short_walks_possible = (total_work_hours_per_day * 60) // short_walk_time // max_dogs_per_walk
    daily_long_walks_possible = 6
    daily_income = (daily_short_walks_possible * short_walk_pay * short_walk_time / 60) + (daily_long_walks_possible * long_walk_pay)
    weekly_income = daily_income * total_work_days_per_week
    result = weekly_income
    return result

print(solution())