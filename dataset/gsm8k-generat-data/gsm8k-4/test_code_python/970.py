def solution():
    """Johann and two friends are to deliver 180 pieces of certified mail. His friends each deliver 41 pieces of mail. How many pieces of mail does Johann need to deliver?"""
    # Define the total number of pieces of mail to be delivered
    total_mail = 180

    # Define the number of pieces of mail each friend delivers
    friend_mail = 41

    # Calculate the total number of pieces of mail Johann needs to deliver
    johann_mail = total_mail - (2 * friend_mail)

    # Return the result
    result = johann_mail
    return result

print(solution())