def solution():
    num_emails = 400
    num_trash_emails = num_emails / 2  # Half of the emails go to trash
    num_remaining_emails = num_emails - num_trash_emails
    num_work_emails = num_remaining_emails * 0.4  # 40% of remaining emails go to work folder
    num_emails_left = num_remaining_emails - num_work_emails
    result = num_emails_left
    return result

print(solution())