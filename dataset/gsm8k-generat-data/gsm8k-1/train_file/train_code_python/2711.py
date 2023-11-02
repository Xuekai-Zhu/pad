def solution():
    """Caprice is taking piano lessons. Her mother pays the teacher $10 for every half-hour of teaching her daughter. If Caprice is taking one lesson per week, and the lesson lasts 1 hour, how much money would the teacher earn in 5 weeks?"""
    lesson_length_in_hours = 1
    lesson_frequency_in_weeks = 1
    teaching_minutes_per_week = lesson_length_in_hours * 60 * lesson_frequency_in_weeks
    amount_per_minute = 10 / 30
    total_income = teaching_minutes_per_week * amount_per_minute * 5
    result = total_income
    return result

print(solution())