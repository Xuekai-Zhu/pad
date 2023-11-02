def solution():
    initial_emails = 0
    deleted_emails1 = 50
    received_emails1 = 15
    deleted_emails2 = 20
    received_emails2 = 5
    new_emails = 10

    # Calculate the total number of emails deleted and received in the first round
    net_emails1 = received_emails1 - deleted_emails1

    # Calculate the total number of emails deleted and received in the second round
    net_emails2 = received_emails2 - deleted_emails2

    # Calculate the total number of remaining emails after deleting all old emails and adding new ones
    total_emails = initial_emails + net_emails1 + net_emails2 + new_emails
    result = total_emails
    return result

print(solution())