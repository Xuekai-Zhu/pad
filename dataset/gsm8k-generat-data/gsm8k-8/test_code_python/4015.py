def solution():
    # Initialize the number of deleted and received emails
    deleted = 0
    received = 0

    # Delete 50 emails and receive 15
    deleted += 50
    received += 15

    # Delete 20 more emails and receive 5
    deleted += 20
    received += 5

    # Calculate the number of new emails left
    new_emails = received - deleted + 10
    result = new_emails
    return result

print(solution())