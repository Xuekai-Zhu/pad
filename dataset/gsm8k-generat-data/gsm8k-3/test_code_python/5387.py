def solution():
    """Jimmy's father receives 20 emails a day. Halfway through April, he subscribed to a news channel that sent 5 more emails per day to his email. What's the total number of emails Jimmy's father had at the end of the month?"""
    # Define the number of days in April and the original daily email count
    APRIL_DAYS = 30
    ORIGINAL_EMAIL_COUNT = 20

    # Calculate the number of days before the subscription
    days_before_subscription = APRIL_DAYS // 2

    # Calculate the number of emails before the subscription
    emails_before_subscription = ORIGINAL_EMAIL_COUNT * days_before_subscription

    # Calculate the number of days after the subscription
    days_after_subscription = APRIL_DAYS - days_before_subscription

    # Define the increased email count after subscription
    INCREASED_EMAIL_COUNT = 5

    # Calculate the number of emails after the subscription
    emails_after_subscription = (ORIGINAL_EMAIL_COUNT + INCREASED_EMAIL_COUNT) * days_after_subscription

    # Calculate the total number of emails
    total_emails = emails_before_subscription + emails_after_subscription

    # Display the total number of emails
    result = total_emails
    return result

print(solution())