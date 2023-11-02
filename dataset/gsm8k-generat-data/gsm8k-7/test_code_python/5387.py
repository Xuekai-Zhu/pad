def solution():
    num_emails_per_day = 20
    initial_num_days = 15  # Halfway through April
    extra_emails_per_day = 5
    remaining_num_days = 15

    # Calculate the total number of emails received before subscribing to the news channel
    total_initial_emails = num_emails_per_day * initial_num_days

    # Calculate the total number of emails received after subscribing to the news channel
    total_extra_emails = (num_emails_per_day + extra_emails_per_day) * remaining_num_days

    # Calculate the total number of emails received at the end of the month
    total_emails = total_initial_emails + total_extra_emails
    result = total_emails
    return result

print(solution())