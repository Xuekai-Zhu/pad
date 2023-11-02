def solution():
    """Steve has 400 new emails in his inbox. He moves half of them to the trash, and 40 percent of the remaining emails to his work folder. How many emails are left in the inbox?"""
    # Define the initial number of emails
    initial_emails = 400

    # Move half of the emails to trash
    trashed_emails = initial_emails / 2

    # Calculate the remaining unread emails
    remaining_emails = initial_emails - trashed_emails

    # Move 40% of remaining emails to work folder
    work_emails = remaining_emails * 0.4

    # Calculate the number of emails left in the inbox
    inbox_emails = remaining_emails - work_emails

    result = inbox_emails
    return result

print(solution())