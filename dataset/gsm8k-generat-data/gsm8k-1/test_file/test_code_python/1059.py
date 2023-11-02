def solution():
    """James gets 80 emails a day. 20% of those emails don't require any response. He responds to the rest of them. How many emails does he respond to in a 5 day work week?"""
    emails_per_day = 80
    non_response_percent = 20
    response_percent = 100 - non_response_percent
    response_emails_per_day = emails_per_day * (response_percent / 100)
    response_emails_per_week = response_emails_per_day * 5
    result = response_emails_per_week
    return result

print(solution())