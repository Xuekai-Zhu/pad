def solution():
    # Calculate the total number of messages sent on the first 3 days
    total_messages = 300 + 200 + 300

    # Calculate the number of messages sent on Wednesday
    wednesday_messages = total_messages + 300

    # Calculate the number of messages sent on Thursday
    thursday_messages = 2 * wednesday_messages

    # Calculate the total number of messages sent
    total_messages += wednesday_messages + thursday_messages
    result = total_messages
    return result

print(solution())