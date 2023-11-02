def solution():
    """To make a living, Carl needs to drive a car for 2 hours every day. After he got promoted he needs to drive for 6 more hours every week. How many hours will Carl drive in two weeks?"""
    daily_hours = 2
    extra_hours_weekly = 6
    total_hours_weekly = daily_hours * 7 + extra_hours_weekly
    total_hours_2weeks = total_hours_weekly * 2
    result = total_hours_2weeks
    return result

print(solution())