def solution():
    """Kim sleeps from 10 p.m. to 6 a.m. and wakes up for 23 minutes at 2:10 a.m. How many minutes did she sleep on her bed that day?"""
    total_sleep_time = 8 * 60
    bathroom_break = 5
    sleepwalking_time = 23
    actual_sleep_time = total_sleep_time - bathroom_break - sleepwalking_time
    result = actual_sleep_time
    return result

print(solution())