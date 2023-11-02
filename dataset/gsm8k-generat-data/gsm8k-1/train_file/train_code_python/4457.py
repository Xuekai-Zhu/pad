def solution():
    """If the normal hours of operation of Jean's business are 4 pm to 10p every day Monday through Friday, and from 6 pm to 10 pm on weekends, how many hours is the business open in a week?"""
    weekday_hours = (10 - 4) * 5 # 6 hours per weekday
    weekend_hours = (10 - 6) * 2 # 4 hours per weekend day
    total_hours = weekday_hours + weekend_hours
    result = total_hours
    return result

print(solution())