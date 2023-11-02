def solution():
    """It takes Polly 20 minutes to cook breakfast every day. She spends 5 minutes cooking lunch. She spends 10 minutes cooking dinner 4 days this week. The rest of the days she spends 30 minutes cooking dinner. How many minutes does Polly spend cooking this week?"""
    # Define the time it takes Polly to cook each meal
    breakfast_time = 20
    lunch_time = 5
    normal_dinner_time = 30
    special_dinner_time = 10

    # Calculate the total time Polly spends cooking dinner
    total_special_dinner_time = special_dinner_time * 4
    total_normal_dinner_time = normal_dinner_time * 3

    # Calculate the total time Polly spends cooking this week
    total_cooking_time = breakfast_time * 7 + lunch_time * 7 + total_special_dinner_time + total_normal_dinner_time

    # return the result
    result = total_cooking_time
    return result

print(solution())