def solution():
    """It takes Polly 20 minutes to cook breakfast every day. She spends 5 minutes cooking lunch. She spends 10 minutes cooking dinner 4 days this week. The rest of the days she spends 30 minutes cooking dinner. How many minutes does Polly spend cooking this week?"""
    # Define the time spent cooking each meal
    BREAKFAST_TIME = 20
    LUNCH_TIME = 5
    SHORT_DINNER_TIME = 10
    LONG_DINNER_TIME = 30

    # Calculate the total time spent cooking dinner
    short_dinner_days = 4
    long_dinner_days = 7 - short_dinner_days
    total_dinner_time = (short_dinner_days * SHORT_DINNER_TIME) + (long_dinner_days * LONG_DINNER_TIME)

    # Calculate the total time spent cooking
    total_time = (BREAKFAST_TIME * 7) + (LUNCH_TIME * 7) + total_dinner_time

    # Display the total time spent cooking
    result = total_time
    return result

print(solution())