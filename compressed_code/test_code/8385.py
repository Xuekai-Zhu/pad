def solution():
    
    old_messages = 20
    new_messages = 55
    unintended_messages = new_messages - old_messages
    messages_per_week = unintended_messages * 7
    result = messages_per_week
    return result

print(solution())