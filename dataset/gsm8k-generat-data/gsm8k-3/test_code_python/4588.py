def solution():
    """A business executive is going on a four day vacation where he will be unable to answer emails.  The first day he is gone, he receives 16 new emails.  On each of the following days, he receives half as many new emails as he received on the prior day.  At the end of his four day vacation, how many new emails will he have received in total?"""
    # Define the number of new emails on the first day
    day1 = 16

    # Define the number of new emails on the subsequent days
    day2 = day1/2
    day3 = day2/2
    day4 = day3/2

    # Calculate the total number of new emails received
    total_emails = day1 + day2 + day3 + day4

    # Display the total number of new emails received
    result = total_emails
    return result

print(solution())