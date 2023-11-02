def solution():
    # Calculate the number of messages sent on Wednesday
    messages_wednesday = 200 + 300

    # Calculate the number of messages sent on Thursday
    messages_thursday = 2 * messages_wednesday

    # Calculate the total number of messages sent in the four days
    total_messages = 300 + 200 + messages_wednesday + messages_thursday
    result = total_messages
    return result

print(solution())