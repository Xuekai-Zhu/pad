def solution():
    """Jean is a customer service rep and answered 35 phone calls on Monday. On Tuesday, she answered 46 and took 27 calls on Wednesday. On Thursday she answered 61 calls and finished off answering 31 calls on Friday. What’s the average number of calls she answers per day?"""
    calls_monday = 35
    calls_tuesday = 46
    calls_wednesday = 27
    calls_thursday = 61
    calls_friday = 31
    total_calls = calls_monday + calls_tuesday + calls_wednesday + calls_thursday + calls_friday
    days_worked = 5
    average_calls = total_calls / days_worked
    result = average_calls
    return result

print(solution())