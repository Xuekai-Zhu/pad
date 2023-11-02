def solution():
    """Rafael works 10 hours on Monday and 8 hours on Tuesday on his delivery job. With 20 hours left to work in the week, how much money does Rafael make if he is paid $20 per hour?"""
    # Define Rafael's work hours
    monday_hours = 10
    tuesday_hours = 8
    remaining_hours = 20

    # Define Rafael's hourly rate
    hourly_rate = 20

    # Calculate Rafael's total pay
    total_pay = (monday_hours + tuesday_hours + remaining_hours) * hourly_rate

    # Display Rafael's total pay
    result = total_pay
    return result

print(solution())