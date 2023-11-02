def solution():
    """To make a living, Carl needs to drive a car for 2 hours every day. After he got promoted he needs to drive for 6 more hours every week. How many hours will Carl drive in two weeks?"""
    daily_hours = 2
    weekly_promotion_hours = 6
    total_hours_in_week = daily_hours * 7 + weekly_promotion_hours
    total_hours_in_two_weeks = total_hours_in_week * 2
    result = total_hours_in_two_weeks
    return result

print(solution())