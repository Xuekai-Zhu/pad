def solution():
    """Jason sent 220 text messages on Monday, half as many text messages on Tuesday, and 50 text messages each day Wednesday through Friday. How many text messages did he send on average during those five days?"""
    # Define the number of text messages sent each day
    monday_messages = 220
    tuesday_messages = monday_messages / 2
    wednesday_messages = 50
    thursday_messages = 50
    friday_messages = 50

    # Calculate the total number of text messages sent over the five days
    total_messages = monday_messages + tuesday_messages + wednesday_messages + thursday_messages + friday_messages

    # Calculate the average number of text messages sent per day
    average_messages = total_messages / 5

    # Display the average number of text messages
    result = average_messages
    return result

print(solution())