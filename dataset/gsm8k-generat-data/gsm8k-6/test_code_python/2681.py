def solution():
    # Calculate Jonathan's daily caloric intake and deficit
    daily_intake = 2500  # calories
    saturday_intake = 3500  # 2500 + 1000 extra calories consumed on Saturday
    daily_burned = 3000  # calories burned per day
    daily_deficit = daily_intake - daily_burned  # calories per day
    saturday_deficit = saturday_intake - daily_burned  # calories on Saturday

    # Calculate Jonathan's weekly caloric deficit
    weekly_deficit = 6 * daily_deficit + saturday_deficit  # assuming six non-Saturday days in a week
    result = weekly_deficit
    return result

print(solution())