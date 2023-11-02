def solution():
     total_emails = 400
     emails_to_trash = total_emails / 2
     emails_to_work_folder = (total_emails - emails_to_trash) * 0.4
     emails_left_in_inbox = total_emails - (emails_to_trash + emails_to_work_folder)
     result = emails_left_in_inbox
     return result

print(solution())