def solution():
    """Joey needs to take a new prescription. The first day he needs to take one pill. Each day he must take two more pills than the previous day. How many pills will he take in a week?"""
    pills_first_day = 1
    pills_per_day_increase = 2
    days_in_week = 7
    pills_in_week = pills_first_day
    for i in range(1, days_in_week):
        pills_on_day_i = pills_first_day + i * pills_per_day_increase
        pills_in_week += pills_on_day_i
    result = pills_in_week
    return result

print(solution())