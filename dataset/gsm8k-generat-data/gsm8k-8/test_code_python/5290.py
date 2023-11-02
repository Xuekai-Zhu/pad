def solution():
    # Define the number of spam emails and calculate the remaining emails
    spam_emails = 400 / 4
    remaining_emails = 400 - spam_emails

    # Calculate the number of promotional messages and the remaining important emails
    promo_messages = 2/5 * remaining_emails
    important_emails = remaining_emails - promo_messages
    result = important_emails
    return result

print(solution())