def solution():
    """James is in charge of running messages from the office to each teacher's classroom. If he delivers 66 messages to Ms. Thompson and 1/3 as many messages to Mr. Yu, how many messages does he deliver total?"""
    messages_to_thompson = 66
    messages_to_yu = messages_to_thompson / 3
    total_messages = messages_to_thompson + messages_to_yu
    result = total_messages
    return result

print(solution())