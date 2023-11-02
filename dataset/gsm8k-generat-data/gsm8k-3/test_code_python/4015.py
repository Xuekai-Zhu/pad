def solution():
    """Jackson is clearing out his email inbox after noticing he has a whole lot of emails that he no longer needs and can delete. While he is cleaning his inbox, though, he keeps getting more emails. While he deletes 50 emails he gets another 15 sent to him. While he deletes 20 more he receives 5 more emails. After he is done deleting all his old emails he has just the new emails left, including 10 more that were sent to him. How many emails are there in Jackson's inbox now?"""
    
    # Total number of emails Jackson had initially
    initial_emails = 0
    
    # While deleting 50 emails, he gets 15 new emails
    initial_emails += 15
    
    # After deleting 20 more emails, he gets 5 new emails
    initial_emails += 5
    
    # After deleting all old emails, he is left with only new emails, including 10 more sent to him
    total_emails = initial_emails - 50 - 20 + 10
    
    result = total_emails
    return result

print(solution())