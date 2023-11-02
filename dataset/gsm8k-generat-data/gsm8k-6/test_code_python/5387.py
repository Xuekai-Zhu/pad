def solution():
    # Calculate the number of days in April
    days_in_April = 30

    # Calculate the total number of emails Jimmys father received in the first half of April
    total_emails = 20 * (days_in_April/2)

    # Calculate the total number of emails Jimmys father received in the second half of April
    extra_emails = (20 + 5) * (days_in_April/2)

    # Calculate the total number of emails Jimmys father received in April
    total_emails += extra_emails

    result = total_emails
    return result

print(solution())