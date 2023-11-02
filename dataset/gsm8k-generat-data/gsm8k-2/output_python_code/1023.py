def solution():
    """Rafael works 10 hours on Monday and 8 hours on Tuesday on his delivery job. With 20 hours left to work in the week, how much money does Rafael make if he is paid $20 per hour?"""
    monday_hours = 10
    tuesday_hours = 8
    remaining_hours = 20
    total_hours = monday_hours + tuesday_hours + remaining_hours
    hourly_rate = 20
    total_pay = total_hours * hourly_rate
    result = total_pay
    return result

print(solution())