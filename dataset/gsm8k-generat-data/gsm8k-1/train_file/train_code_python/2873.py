def solution():
    """Jason sent 220 text messages on Monday, half as many text messages on Tuesday, and 50 text messages each day Wednesday through Friday. How many text messages did he send on average during those five days?"""
    monday_messages = 220
    tuesday_messages = monday_messages / 2
    wednesday_friday_messages = 50 * 3
    total_messages = monday_messages + tuesday_messages + wednesday_friday_messages
    average_messages = total_messages / 5
    result = average_messages
    
    return result

print(solution())