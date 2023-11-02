def solution():
    monday = 220
    tuesday = monday/2
    wednesday = 50
    thursday = 50
    friday = 50

    # Calculate the total number of text messages
    total_messages = monday + tuesday + wednesday + thursday + friday

    # Calculate the average number of text messages per day
    average_messages = total_messages / 5
    result = average_messages
    return result

print(solution())