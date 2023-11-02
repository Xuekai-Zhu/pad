def solution():
    """Marie has 98 unread messages on her phone. She decides to clear them by reading 20 messages a day. However, she also gets 6 new messages a day. How many days will it take her to read all her unread messages?"""
    # Define the number of unread messages and the number of messages read and received per day
    unread_messages = 98
    messages_read_per_day = 20
    messages_received_per_day = 6

    # Initialize the number of days it will take to read all the messages
    days = 0

    # Loop until all messages have been read
    while unread_messages > 0:
        # Read the daily number of messages and subtract them from the unread messages
        unread_messages -= messages_read_per_day
        # Add the daily number of new messages
        unread_messages += messages_received_per_day
        # Increment the number of days
        days += 1

    # Display the number of days it took to read all the messages
    result = days
    return result

print(solution())