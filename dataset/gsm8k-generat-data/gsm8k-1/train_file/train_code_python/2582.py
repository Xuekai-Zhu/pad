def solution():
    """Cindy was hired to teach 4 math courses which required her to be in the classroom for 48 hours a week altogether. How much did Cindy earn for teaching 1 math course in a month with exactly 4 weeks if her hourly rate per class is $25?"""
    hours_per_week = 48
    courses_per_week = 4
    total_hours = hours_per_week * 4
    hourly_rate = 25
    earnings_per_course = total_hours / courses_per_week * hourly_rate
    result = earnings_per_course
    return result

print(solution())