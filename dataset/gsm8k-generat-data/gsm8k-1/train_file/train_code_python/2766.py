def solution():
    """It takes Polly 20 minutes to cook breakfast every day. 
    She spends 5 minutes cooking lunch. She spends 10 minutes cooking dinner 4 days this week. 
    The rest of the days she spends 30 minutes cooking dinner. How many minutes does Polly spend cooking this week?"""
    minutes_breakfast = 20
    minutes_lunch = 5
    minutes_dinner_4_days = 10
    minutes_dinner_rest_days = 30
    days_dinner_4 = 4
    days_dinner_rest = 7 - days_dinner_4
    minutes_breakfast_week = 7 * minutes_breakfast
    minutes_lunch_week = 7 * minutes_lunch
    minutes_dinner_4_week = days_dinner_4 * minutes_dinner_4_days
    minutes_dinner_rest_week = days_dinner_rest * minutes_dinner_rest_days
    total_minutes_week = minutes_breakfast_week + minutes_lunch_week + minutes_dinner_4_week + minutes_dinner_rest_week
    result = total_minutes_week
    return result

print(solution())