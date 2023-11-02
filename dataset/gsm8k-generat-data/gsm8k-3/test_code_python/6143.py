def solution():
    """Steve has 400 new emails in his inbox. He moves half of them to the trash, and 40% of the remaining emails to his work folder. How many emails are left in the inbox?"""
    # Define the number of emails in Steve's inbox
    emails_inbox = 400

    # Calculate the number of emails moved to trash
    emails_trash = emails_inbox / 2

    # Calculate the number of emails remaining in Steve's inbox
    emails_remaining = emails_inbox - emails_trash

    # Calculate the number of emails moved to work folder
    emails_work = emails_remaining * 0.4

    # Calculate the number of emails left in Steve's inbox
    emails_left = emails_remaining - emails_work

    # Display the number of emails left in Steve's inbox
    result = emails_left
    return result

print(solution())