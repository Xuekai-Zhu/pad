def solution():
    """Olivia earns $9 per hour. She worked 4 hours on Monday, 3 hours on Wednesday and 6 hours on Friday. How much money did Olivia make this week?"""
    hourly_rate = 9
    monday_hours = 4
    wednesday_hours = 3
    friday_hours = 6
    total_hours = monday_hours + wednesday_hours + friday_hours
    total_earned = total_hours * hourly_rate
    result = total_earned
    return result

print(solution())