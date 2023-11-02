def solution():
    """Marie has 98 unread messages on her phone. She decides to clear them by reading 20 messages a day. However, she also gets 6 new messages a day. How many days will it take her to read all her unread messages?"""
    unread_messages = 98
    messages_read_per_day = 20
    new_messages_per_day = 6
    days_to_read = (unread_messages / messages_read_per_day) + (unread_messages % messages_read_per_day > 0)
    total_messages_received = new_messages_per_day * days_to_read
    result = days_to_read + ((unread_messages + total_messages_received) / messages_read_per_day) + ((unread_messages + total_messages_received) % messages_read_per_day > 0)
    return result

print(solution())