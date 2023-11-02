def solution():
    total_emails = 400
    spam_emails = total_emails / 4
    promotional_emails = (total_emails - spam_emails) / 5
    important_emails = total_emails - spam_emails - promotional_emails
    result = important_emails
    
    return result

print(solution())