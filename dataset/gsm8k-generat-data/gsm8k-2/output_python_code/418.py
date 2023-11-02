def solution():
    """Kenny played 10 hours of basketball last week. He ran for twice as long as he played basketball, and he practiced on the trumpet for twice as long as he ran. How many hours did Kenny practice on the trumpet last week?"""
    basketball_time = 10
    running_time = basketball_time * 2
    trumpet_time = running_time * 2
    total_time = basketball_time + running_time + trumpet_time
    trumpet_hours = trumpet_time
    result = trumpet_hours
    return result

print(solution())