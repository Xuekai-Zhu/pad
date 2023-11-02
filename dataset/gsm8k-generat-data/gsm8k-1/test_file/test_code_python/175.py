def solution():
    """Lloyd earns $10 an hour on Math tutoring. He tutored 5 hours for the first week and 8 hours for the second week. How much did he earn for the first two weeks?"""
    hourly_rate = 10
    hours_week_one = 5
    hours_week_two = 8
    total_hours = hours_week_one + hours_week_two
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())