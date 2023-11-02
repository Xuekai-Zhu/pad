def solution():
    """Marie has 98 unread messages on her phone. She decides to clear them by reading 20 messages a day. However, she also gets 6 new messages a day. How many days will it take her to read all her unread messages?"""
    # Define the number of initial unread messages and the number of new messages received per day
    initial_messages = 98
    new_messages_per_day = 6

    # Define the number of messages read per day
    messages_read_per_day = 20

    # Initialize the day counter and the number of remaining messages
    days = 0
    remaining_messages = initial_messages

    # Loop until all messages are read
    while remaining_messages > 0:
        # Increment the day counter
        days += 1

        # Update the number of remaining messages
        remaining_messages -= messages_read_per_day

        # Add the new messages received to the remaining messages
        remaining_messages += new_messages_per_day

    # Display the number of days it took to read all the messages
    result = days
    return result

print(solution())