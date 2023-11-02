def solution():
    """Sadie slept 8 hours on Monday. For the next two days, she slept 2 hours less, each, because she had to complete some assignments. If the rest of the week she slept 1 hour more than those two days, how many hours did she sleep in total throughout the week?"""
    monday_sleep = 8
    tuesday_sleep = monday_sleep - 2
    wednesday_sleep = tuesday_sleep - 2
    remaining_days_sleep = wednesday_sleep + 1
    total_sleep = monday_sleep + tuesday_sleep + wednesday_sleep + remaining_days_sleep * 4
    result = total_sleep
    return result

print(solution())