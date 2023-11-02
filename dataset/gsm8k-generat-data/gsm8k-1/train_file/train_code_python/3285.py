def solution():
    """John decides to get a new phone number and it ends up being a recycled number. He used to get 20 text messages a day. Now he is getting 55. Assuming the number of texts his friends send has not changed, how many text messages per week is he getting that are not intended for him?"""
    old_messages = 20
    new_messages = 55
    unintended_messages = new_messages - old_messages
    messages_per_week = unintended_messages * 7
    result = messages_per_week
    return result

print(solution())