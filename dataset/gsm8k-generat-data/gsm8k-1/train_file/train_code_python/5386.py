def solution():
    """Jimmy's father receives 20 emails a day. Halfway through April, he subscribed to a news channel that sent 5 more emails per day to his email. What's the total number of emails Jimmy's father had at the end of the month?"""
    daily_emails = 20
    additional_emails = 5
    days_in_month = 30
    halfway_through = days_in_month // 2
    total_emails = (daily_emails * halfway_through) + ((daily_emails + additional_emails) * (days_in_month - halfway_through))
    result = total_emails
    return result

print(solution())