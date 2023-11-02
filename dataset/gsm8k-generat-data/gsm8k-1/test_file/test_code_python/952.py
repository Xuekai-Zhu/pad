def solution():
    """Robyn sends sixteen emails a day. Seven are work emails, and two-thirds of the remainder are to family. One-third of the other emails are to her boyfriend. How many emails a day does she send to her boyfriend?"""
    total_emails = 16
    work_emails = 7
    non_work_emails = total_emails - work_emails
    family_emails = (2/3) * non_work_emails
    remaining_emails = non_work_emails - family_emails
    boyfriend_emails = remaining_emails / 3
    result = boyfriend_emails
    return result

print(solution())