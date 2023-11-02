def solution():
    """Mindy has 7 less than 9 times as many emails waiting for her as phone messages. If she has a total of 93 emails and phone messages combined, how many emails does she have?"""
    total_messages = 93
    email_messages = (total_messages - 7) / 9
    result = email_messages
    return result

print(solution())