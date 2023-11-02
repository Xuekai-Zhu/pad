def solution():
    
    monday_messages = 220
    tuesday_messages = monday_messages / 2
    wed_fri_messages = 50 * 3
    total_messages = monday_messages + tuesday_messages + wed_fri_messages
    average_messages = total_messages / 5
    result = average_messages
    return result

print(solution())