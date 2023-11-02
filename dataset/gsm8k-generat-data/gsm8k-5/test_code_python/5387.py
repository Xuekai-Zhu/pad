def solution():
    emails_per_day = 20  # Jimmy's father receives 20 emails a day
    days_in_half_month = 15  # Halfway through April, Jimmy's father subscribed to the news channel
    extra_emails_per_day = 5  # After subscribing to the news channel, Jimmy's father received 5 more emails per day

    # Calculate the total number of emails before subscribing to the news channel
    total_emails_before = emails_per_day * days_in_half_month

    # Calculate the total number of emails after subscribing to the news channel
    total_emails_after = (emails_per_day + extra_emails_per_day) * (30 - days_in_half_month)

    # Calculate the total number of emails for the whole month
    total_emails = total_emails_before + total_emails_after
    result = total_emails
    return result

print(solution())