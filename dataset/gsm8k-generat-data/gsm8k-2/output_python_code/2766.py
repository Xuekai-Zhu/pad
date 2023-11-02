def solution():
    """It takes Polly 20 minutes to cook breakfast every day. She spends 5 minutes cooking lunch. She spends 10 minutes cooking dinner 4 days this week. The rest of the days she spends 30 minutes cooking dinner. How many minutes does Polly spend cooking this week?"""
    breakfast_time = 20 * 7
    lunch_time = 5 * 7
    dinner_time = (10 * 4) + (30 * 3) # 3 days left in the week
    total_time = breakfast_time + lunch_time + dinner_time
    result = total_time
    return result

print(solution())