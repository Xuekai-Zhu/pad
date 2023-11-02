def solution():
    """A Whatsapp group has members sending messages every day sharing about how each one's day was. Last week, 300 messages were sent by the members on Monday, 200 messages on Tuesday, 300 more messages on Wednesday than the previous day, and two times as many messages on Thursday as there were on Wednesday. Calculate the number of messages sent in the Whatsapp group after the four days."""
    # Define the number of messages sent on Monday and Tuesday
    monday_messages = 300
    tuesday_messages = 200

    # Calculate the number of messages sent on Wednesday
    wednesday_messages = tuesday_messages + 300

    # Calculate the number of messages sent on Thursday
    thursday_messages = wednesday_messages * 2

    # Calculate the total number of messages sent in the group after the four days
    total_messages = monday_messages + tuesday_messages + wednesday_messages + thursday_messages

    # return the result
    result = total_messages
    return result

print(solution())