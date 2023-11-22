def solution():
    
    # Define the number of days in a week
    DAYS_IN_WEEK = 5

    # Define the number of emails James gets each day
    emails_per_day = 80

    # Calculate the number of emails that don't require any response
    no_response_emails = emails_per_day * 0.2

    # Calculate the number of emails that James responds to
    response_emails = emails_per_day - no_response_emails

    # Display the number of emails that James responds to
    result = response_emails
    return result

print(solution())