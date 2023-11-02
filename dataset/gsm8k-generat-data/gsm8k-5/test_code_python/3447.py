def solution():
    chandler_weekly_consumption = 23  # Chandler can eat a total of 23 apples per week
    lucy_weekly_consumption = 19  # Lucy can eat a total of 19 apples per week
    apples_required_per_month = (chandler_weekly_consumption + lucy_weekly_consumption) * 4  # The farmer delivers once per month

    result = apples_required_per_month
    return result

print(solution())