def solution():
    """Jackson is clearing out his email inbox after noticing he has a whole lot of emails that he no longer needs and can delete. While he is cleaning his inbox, though, he keeps getting more emails. While he deletes 50 emails he gets another 15 sent to him. While he deletes 20 more he receives 5 more emails. After he is done deleting all his old emails he has just the new emails left, including 10 more that were sent to him. How many emails are there in Jackson's inbox now?"""
    initial_emails = 50
    additional_emails_1 = 15
    deleted_emails = 20
    additional_emails_2 = 5
    new_emails = 10
    total_emails = initial_emails + additional_emails_1 - deleted_emails + additional_emails_2 + new_emails
    result = total_emails
    return result

print(solution())