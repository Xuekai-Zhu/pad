def solution():
    """In preparation for his mountain climbing, Arvin wants to run a total of 20 kilometers in a week. On the first day, he ran 2 kilometers. On each subsequent day, he increased his running distance by 1 kilometer over the previous day. If he runs for 5 days a week, how many kilometers did he run on the 5th day?"""
    total_distance = 20
    first_day_distance = 2
    days_of_running = 5
    total_distance -= first_day_distance
    for i in range(2, days_of_running + 1):
        total_distance -= (first_day_distance + (i - 1))

    fifth_day_distance = first_day_distance + (days_of_running - 1)
    result = fifth_day_distance
    return result

print(solution())