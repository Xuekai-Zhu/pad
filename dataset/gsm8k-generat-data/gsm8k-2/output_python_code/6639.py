def solution():
    """Noah, who loves his Grammy, calls her every week to talk about his day. If each call lasts 30 minutes and he is charged $0.05 per call minute, how much would he be billed if he makes the calls for a year?"""
    call_duration = 30
    cost_per_minute = 0.05
    calls_per_week = 1
    weeks_per_year = 52
    total_duration = call_duration * calls_per_week * weeks_per_year
    total_cost = total_duration * cost_per_minute
    result = total_cost
    return result

print(solution())