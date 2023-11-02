def solution():
    # Set up equation for the number of emails Mindy has
    # Let x be the number of phone messages Mindy has
    # Then the number of emails she has is 9x - 7
    # The total number of emails and phone messages is 93, so we have:
    # x + (9x - 7) = 93
    # Solving for x gives us the number of phone messages
    x = (93 + 7) / 10
    # The number of emails is 9 times the number of phone messages, minus 7
    num_emails = 9 * x - 7
    result = num_emails
    return result

print(solution())