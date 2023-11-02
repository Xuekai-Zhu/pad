def solution():
    # Calculate the total number of text messages sent in five days
    total_messages = 220 + 220/2 + 50*3  # 220 on Monday, half as many on Tuesday, 50 each on Wednesday, Thursday, and Friday
    average_messages = total_messages / 5  # Calculate the average number of messages per day
    result = average_messages
    return result

print(solution())