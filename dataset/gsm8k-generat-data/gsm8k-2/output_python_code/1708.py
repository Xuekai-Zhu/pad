def solution():
    """A Whatsapp group has members sending messages every day sharing about how each one's day was. Last week, 300 messages were sent by the members on Monday, 200 messages on Tuesday, 300 more messages on Wednesday than the previous day, and two times as many messages on Thursday as there were on Wednesday. Calculate the number of messages sent in the Whatsapp group after the four days."""
    mon_messages = 300
    tues_messages = 200
    wed_messages = tues_messages + 300
    thurs_messages = 2 * wed_messages
    total_messages = mon_messages + tues_messages + wed_messages + thurs_messages
    result = total_messages
    return result

print(solution())