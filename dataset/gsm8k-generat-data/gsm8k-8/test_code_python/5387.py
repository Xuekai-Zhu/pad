def solution():
    # Calculate the total number of days in April
    total_days = 30

    # Calculate the total number of normal emails received in April
    normal_emails = 20 * total_days / 2

    # Calculate the total number of news channel emails received in April
    news_emails = (20 + 5) * total_days / 2

    # Calculate the total number of emails received in April
    total_emails = normal_emails + news_emails

    result = total_emails
    return result

print(solution())