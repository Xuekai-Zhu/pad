def solution():
    # Calculate the total number of loaves of bread baked in one day
    daily_breads = 5 * 4  # 5 loaves per hour in 4 ovens
    weekdays_breads = daily_breads * 5  # breads baked from Monday to Friday
    weekends_breads = daily_breads * 2 * 2  # breads baked on Saturday and Sunday
    total_breads = weekdays_breads + weekends_breads  # total breads baked in a week
    total_breads_3_weeks = total_breads * 3  # total breads baked in 3 weeks
    result = total_breads_3_weeks
    return result

print(solution())