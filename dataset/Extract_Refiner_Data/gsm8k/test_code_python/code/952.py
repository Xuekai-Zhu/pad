def solution():
    
    # Define the number of work emails
    work_emails = 7

    # Calculate the remainder of emails
    remainder_emails = 16 - work_emails

    # Calculate the number of emails to family
    family_emails = remainder_emails * (2/3)

    # Calculate the number of emails to boyfriend
    boyfriend_emails = remainder_emails * (1/3)

    # Display the number of emails to boyfriend
    result = boyfriend_emails
    return result

print(solution())