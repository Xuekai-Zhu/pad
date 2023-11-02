def solution():
    # Define the variables
    total_emails = 400
    trash_emails = total_emails / 2
    remaining_emails = total_emails - trash_emails
    work_emails = 0.4 * remaining_emails

    # Calculate the final number of emails in the inbox
    final_emails = remaining_emails - work_emails
    result = final_emails
    return result

print(solution())