def solution():
    days_per_week = 7
    weeks_per_year = 52
    total_days = days_per_week * weeks_per_year
    days_without_double_training = 2 * weeks_per_year  # James has 2 rest days per week
    days_with_double_training = total_days - days_without_double_training
    hours_per_day = 4
    total_training_hours = days_with_double_training * 2 * hours_per_day
    result = total_training_hours
    return result

print(solution())