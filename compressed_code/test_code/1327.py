def solution():
    
    mon_messages = 300
    tues_messages = 200
    wed_messages = tues_messages + 300
    thurs_messages = 2 * wed_messages
    total_messages = mon_messages + tues_messages + wed_messages + thurs_messages
    result = total_messages
    return result

print(solution())