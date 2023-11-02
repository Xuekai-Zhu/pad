def solution():
    """A class has 32 students and they all need to present their projects. Every period is 40 minutes long. How many periods will it take for every student to present their project if they have 5 minutes to do so?"""
    total_students = 32
    presentation_time = 5
    period_time = 40
    presentations_per_period = period_time // presentation_time
    periods_needed = total_students / presentations_per_period
    result = periods_needed
    return result

print(solution())