def solution():
    
    lesson_length_in_hours = 1
    lesson_frequency_in_weeks = 1
    teaching_minutes_per_week = lesson_length_in_hours * 60 * lesson_frequency_in_weeks
    amount_per_minute = 10 / 30
    total_income = teaching_minutes_per_week * amount_per_minute * 5
    result = total_income
    return result

print(solution())