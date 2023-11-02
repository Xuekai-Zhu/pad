def solution():
    chandler_weekly_apples = 23
    lucy_weekly_apples = 19
    num_weeks_in_month = 4

    # Calculate the total number of apples Chandler and Lucy can eat in a month
    total_monthly_apples = (chandler_weekly_apples + lucy_weekly_apples) * num_weeks_in_month

    result = total_monthly_apples
    return result

print(solution())