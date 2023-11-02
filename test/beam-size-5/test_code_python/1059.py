def solution():
    # Calculate the number of emails who don't require any response
    no_response_emails = 0.2 * 80

    # Calculate the number of emails who respond to in a day work week
    emails_per_day = 80 - no_response_emails

    # Calculate the number of emails who respond to in a day work week
    emails_per_day_work_week = emails_per_day * 5

    result = emails_per_day_work_week
    return result

print(solution())