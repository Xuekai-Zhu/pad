def solution():
    first_day_emails = 16
    total_emails = first_day_emails

    for i in range(1, 4):
        emails_received = first_day_emails / (2 ** i)
        total_emails += emails_received

    result = total_emails
    return result

print(solution())