def solution():
    """Cindy was hired to teach 4 math courses which required her to be in the classroom for 48 hours a week altogether. How much did Cindy earn for teaching 1 math course in a month with exactly 4 weeks if her hourly rate per class is $25?"""
    total_hours = 48 * 4
    hours_per_math_course = total_hours / 4
    hourly_rate = 25
    earning_per_math_course = hours_per_math_course * hourly_rate
    earning_per_month = earning_per_math_course * 4
    result = earning_per_month
    return result

print(solution())