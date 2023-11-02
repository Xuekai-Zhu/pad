def solution():
    # Calculate the total time Polly spends cooking breakfast
    breakfast_time = 20 * 7

    # Calculate the total time Polly spends cooking lunch
    lunch_time = 5 * 7

    # Calculate the total time Polly spends cooking dinner 4 days a week
    dinner_time_4days = 10 * 4

    # Calculate the total time Polly spends cooking dinner the rest of the days
    dinner_time_rest = 30 * 3

    # Calculate the total time Polly spends cooking this week
    total_time = breakfast_time + lunch_time + dinner_time_4days + dinner_time_rest
    result = total_time
    return result

print(solution())