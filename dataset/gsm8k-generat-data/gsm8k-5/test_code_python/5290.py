def solution():
    total_emails = 400

    # Calculate the number of spam emails
    spam_emails = total_emails * (1/4)

    # Calculate the number of non-spam emails
    non_spam_emails = total_emails - spam_emails

    # Calculate the number of promotional messages
    promotional_emails = non_spam_emails * (2/5)

    # Calculate the number of important emails
    important_emails = non_spam_emails - promotional_emails

    result = important_emails
    return result

print(solution())