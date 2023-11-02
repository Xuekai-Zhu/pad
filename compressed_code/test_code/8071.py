def solution():
    
    monday_messages = 220
    tuesday_messages = monday_messages / 2
    wednesday_friday_messages = 50 * 3
    total_messages = monday_messages + tuesday_messages + wednesday_friday_messages
    average_messages = total_messages / 5
    result = average_messages
    
    return result

print(solution())