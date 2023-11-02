def solution():
    monday_messages = 220
    tuesday_messages = monday_messages / 2
    wednesday_messages = 50
    thursday_messages = 50
    friday_messages = 50

    # Calculate total messages sent during the week
    total_messages = monday_messages + tuesday_messages + wednesday_messages + thursday_messages + friday_messages

    # Calculate average messages per day
    avg_messages_per_day = total_messages / 5
    result = avg_messages_per_day
    return result

print(solution())