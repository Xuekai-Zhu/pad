def solution():
    inbox_emails = 400
    trashed_emails = inbox_emails / 2
    remaining_emails = inbox_emails - trashed_emails
    work_folder_emails = 0.4 * remaining_emails
    remaining_emails = remaining_emails - work_folder_emails
    result = remaining_emails
    return result

print(solution())