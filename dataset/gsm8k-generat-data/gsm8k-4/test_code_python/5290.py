def solution():
    """Out of the 400 emails that Antonia received in her mail, 1/4 were spam emails, while 2/5 of the remaining emails were promotional messages. If the rest of the emails were important emails, calculate the total number of important emails in her inbox."""
    # Define the total number of emails
    total_emails = 400

    # Calculate the number of spam emails
    spam_emails = total_emails * (1/4)

    # Calculate the number of remaining emails after spam
    remaining_emails = total_emails - spam_emails

    # Calculate the number of promotional emails
    promotional_emails = remaining_emails * (2/5)

    # Calculate the number of important emails
    important_emails = total_emails - spam_emails - promotional_emails

    # return the result
    result = important_emails
    return result

print(solution())