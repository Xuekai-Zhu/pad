def solution():
    total_students = 32
    minutes_per_presentation = 5
    minutes_per_period = 40
    presentations_per_period = minutes_per_period // minutes_per_presentation
    total_periods = total_students // presentations_per_period
    result = total_periods
    return result

print(solution())