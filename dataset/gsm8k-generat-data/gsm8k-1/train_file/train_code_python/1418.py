def solution():
    """In preparation for his mountain climbing, Arvin wants to run a total of 20 kilometers in a week. On the first day, he ran 2 kilometers. On each subsequent day, he increased his running distance by 1 kilometer over the previous day. If he runs for 5 days a week, how many kilometers did he run on the 5th day?"""
    total_kilometers = 20
    days_per_week = 5
    starting_distance = 2
    daily_increase = 1
    remaining_kilometers = total_kilometers - starting_distance
    remaining_days = days_per_week - 1
    total_increase = daily_increase * remaining_days
    distance_on_last_day = (remaining_kilometers - total_increase) / remaining_days
    result = distance_on_last_day + daily_increase
    return result

print(solution())