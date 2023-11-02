def solution():
    # Calculate the total number of messages sent in the Whatsapp group after 4 days
    total_messages = 300 + 200 + (300 + 200) + 2*(300 + 300) # 300 messages on Monday, 200 messages on Tuesday, 300 more messages on Wednesday than Tuesday, two times as many messages on Thursday as there were on Wednesday
    result = total_messages
    return result

print(solution())