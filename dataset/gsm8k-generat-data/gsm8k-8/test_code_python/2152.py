def solution():
    # Define the number of jellybeans and the number of recipients
    jellybeans = 70
    recipients = 3 + 2

    # Divide the jellybeans equally among the recipients
    jellybeans_per_recipient = jellybeans // recipients

    # Return the number of jellybeans each recipient received
    result = jellybeans_per_recipient
    return result

print(solution())