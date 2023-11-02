def solution():
    """A Whatsapp group has members sending messages every day sharing about how each one's day was.
    Last week, 300 messages were sent by the members on Monday, 200 messages on Tuesday, 300 more messages on Wednesday than the previous day,
    and two times as many messages on Thursday as there were on Wednesday.
    Calculate the number of messages sent in the Whatsapp group after the four days."""
    
    monday_messages = 300
    tuesday_messages = 200
    wednesday_messages = tuesday_messages + 300
    thursday_messages = wednesday_messages * 2
    
    total_messages = monday_messages + tuesday_messages + wednesday_messages + thursday_messages
    result = total_messages
    return result

print(solution())