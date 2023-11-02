def solution():
    # Calculate the total number of mail items that need stamps
    thanks_cards = 3
    bills = 2
    mail_in_rebates = bills + 3
    job_applications = mail_in_rebates * 2
    total_mail_items = thanks_cards + bills + mail_in_rebates + job_applications
    # Calculate the total number of stamps needed, accounting for the electric bill needing 2 stamps
    stamps = total_mail_items - bills + 2
    result = stamps
    return result

print(solution())