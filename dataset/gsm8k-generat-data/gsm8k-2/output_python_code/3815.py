def solution():
    """Goldie makes $5 an hour for pet-sitting. Last week, she worked for 20 hours while this week, she worked for 30 hours. How much did Goldie earn in two weeks for pet-sitting?"""
    hourly_rate = 5
    week_one_hours = 20
    week_two_hours = 30
    total_hours = week_one_hours + week_two_hours
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())