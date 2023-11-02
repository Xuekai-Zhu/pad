def solution():
    
    inbox_emails = 400
    trash_emails = inbox_emails / 2
    remaining_emails = inbox_emails - trash_emails
    work_emails = 0.4 * remaining_emails
    final_emails = remaining_emails - work_emails
    result = final_emails
    return result

print(solution())