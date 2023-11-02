def solution():
    """Aunt Angela has 70 jellybeans in a jar. She wants to divide them equally and give them to her 3 nephews and 2 nieces. How many jellybeans did each nephew or niece receive?"""
    # Define the number of jellybeans and the number of recipients
    jellybeans = 70
    recipients = 3 + 2

    # Calculate the number of jellybeans each recipient will receive
    jellybeans_per_recipient = jellybeans // recipients

    # Return the result
    result = jellybeans_per_recipient
    return result

print(solution())