def solution():
    total_emails = 400  # Steve has 400 new emails in his inbox
    trash_emails = total_emails / 2  # Steve moves half of the emails to the trash
    remaining_emails = total_emails - trash_emails  # Calculate the number of emails left after moving some to trash
    work_folder_emails = remaining_emails * 0.4  # Steve puts 40% of the remaining emails into his work folder
    inbox_emails = remaining_emails - work_folder_emails  # Calculate the number of emails left in the inbox
    result = inbox_emails
    return result

print(solution())