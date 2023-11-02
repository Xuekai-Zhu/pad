def solution():
    """Steve has 400 new emails in his inbox. He moves half of them to the trash, and 40 percent of the remaining emails to his work folder. How many emails are left in the inbox?"""
    initial_emails = 400
    emails_in_trash = initial_emails / 2
    remaining_emails = initial_emails - emails_in_trash
    work_emails = remaining_emails * 0.4
    remaining_emails = remaining_emails - work_emails
    result = remaining_emails
    return result

print(solution())