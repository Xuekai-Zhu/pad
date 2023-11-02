def solution():
    """Mindy has 7 less than 9 times as many emails waiting for her as phone messages. If she has a total of 93 emails and phone messages combined, how many emails does she have?"""
    # Let x be the number of phone messages
    # Then the number of emails is 9x - 7
    # The total number of messages is x + (9x - 7) = 10x - 7

    # Set up the equation for the total number of messages
    total_messages = 93
    10x - 7 = total_messages

    # Solve for x
    x = (total_messages + 7) / 10

    # Calculate the number of emails
    emails = 9*x - 7

    result = int(emails)
    return result

print(solution())