def solution():
    monday_messages = 300
    tuesday_messages = 200
    wednesday_messages = tuesday_messages + 300
    thursday_messages = 2 * wednesday_messages

    total_messages = monday_messages + tuesday_messages + wednesday_messages + thursday_messages
    result = total_messages
    return result

print(solution())