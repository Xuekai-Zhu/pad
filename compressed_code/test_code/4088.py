def solution():
    
    total_emails = 400
    spam_emails = total_emails // 4
    remaining_emails = total_emails - spam_emails
    promo_emails = (2/5) * remaining_emails
    important_emails = remaining_emails - promo_emails
    result = important_emails
    return result

print(solution())