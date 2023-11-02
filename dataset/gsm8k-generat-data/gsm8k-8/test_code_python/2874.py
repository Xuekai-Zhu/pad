def solution():
    # Calculate the number of text messages on Tuesday
    tuesday_messages = 220 / 2

    # Calculate the total number of text messages for the five days
    total_messages = 220 + tuesday_messages + (50 * 3)

    # Calculate the average number of text messages per day
    average_messages = total_messages / 5
    result = average_messages
    return result

print(solution())