def solution():
    """Olivia earns $9 per hour. She worked 4 hours on Monday, 3 hours on Wednesday and 6 hours on Friday. How much money did Olivia make this week?"""
    hourly_wage = 9
    monday_hours = 4
    wednesday_hours = 3
    friday_hours = 6
    total_hours = monday_hours + wednesday_hours + friday_hours
    weekly_earnings = total_hours * hourly_wage
    result = weekly_earnings
    return result

print(solution())