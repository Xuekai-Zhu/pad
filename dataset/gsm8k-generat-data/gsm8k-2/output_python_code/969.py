def solution():
    """Johann and two friends are to deliver 180 pieces of certified mail. His friends each deliver 41 pieces of mail. How many pieces of mail does Johann need to deliver?"""
    total_mail = 180
    friend_mail = 41
    johann_mail = total_mail - (2 * friend_mail)
    result = johann_mail
    return result

print(solution())