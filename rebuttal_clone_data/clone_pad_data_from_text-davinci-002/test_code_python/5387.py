def solution():
    emails_per_day = 20
    emails_per_day_after_news_subscription = 5
    total_emails_per_day = emails_per_day + emails_per_day_after_news_subscription
    total_emails_in_month = total_emails_per_day * 30
    result = total_emails_in_month
    return result

print(solution())