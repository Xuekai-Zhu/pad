def solution():
    """Out of the 400 emails that Antonia received in her mail, 1/4 were spam emails, while 2/5 of the remaining emails were promotional messages. If the rest of the emails were important emails, calculate the total number of important emails in her inbox."""
    total_emails = 400
    spam_emails = total_emails / 4
    remaining_emails = total_emails - spam_emails
    promotional_emails = 2/5 * remaining_emails
    important_emails = remaining_emails - promotional_emails
    result = important_emails
    return result

print(solution())