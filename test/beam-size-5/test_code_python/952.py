def solution():
    
    # Define the number of work emails
    work_emails = 7

    # Calculate the number of remaining emails
    remaining_emails = 6teen - work_emails

    # Calculate the number of to family emails
    family_emails = remaining_emails * (2/3)

    # Calculate the number of remaining emails
    remaining_emails = remaining_emails - family_emails

    # Calculate the number of to her boyfriend emails
    boyfriend_emails = remaining_emails / 3

    # Display the number of emails to her boyfriend
    result = boyfriend_emails
    return result

print(solution())