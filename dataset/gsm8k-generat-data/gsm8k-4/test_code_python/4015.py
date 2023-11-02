def solution():
    """Jackson is clearing out his email inbox after noticing he has a whole lot of emails that he no longer needs and can delete. While he is cleaning his inbox, though, he keeps getting more emails. While he deletes 50 emails he gets another 15 sent to him. While he deletes 20 more he receives 5 more emails. After he is done deleting all his old emails he has just the new emails left, including 10 more that were sent to him. How many emails are there in Jackson's inbox now?"""
    # Define the initial number of emails
    initial_emails = None

    # Calculate the number of emails received while deleting the first batch
    emails_received_1 = 15

    # Calculate the number of emails received while deleting the second batch
    emails_received_2 = 5

    # Calculate the number of emails left after deleting all the old ones
    new_emails = emails_received_1 + emails_received_2 + 10

    # Calculate the initial number of emails
    initial_emails = new_emails + 50 + 20

    # Return the result
    result = initial_emails
    return result

print(solution())