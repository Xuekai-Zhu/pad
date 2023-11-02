def solution():
    """Rafael works 10 hours on Monday and 8 hours on Tuesday on his delivery job. With 20 hours left to work in the week, how much money does Rafael make if he is paid $20 per hour?"""
    monday_hours = 10
    tuesday_hours = 8
    weekly_hours_left = 20
    hourly_rate = 20
    total_worked_hours = monday_hours + tuesday_hours + weekly_hours_left
    total_earned_money = total_worked_hours * hourly_rate
    result = total_earned_money
    return result

print(solution())