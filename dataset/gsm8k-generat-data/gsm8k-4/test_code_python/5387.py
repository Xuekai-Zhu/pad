def solution():
    """Jimmy's father receives 20 emails a day. Halfway through April, he subscribed to a news channel that sent 5 more emails per day to his email. What's the total number of emails Jimmy's father had at the end of the month?"""
    # Define the initial number of emails
    initial_emails = 20 * 15

    # Define the number of additional emails received after subscribing to the news channel
    additional_emails = 5 * 15

    # Calculate the total number of emails received
    total_emails = initial_emails + additional_emails

    # Return the result
    result = total_emails
    return result

print(solution())