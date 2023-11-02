def solution():
    """Johann and two friends are to deliver 180 pieces of certified mail. His friends each deliver 41 pieces of mail. How many pieces of mail does Johann need to deliver?"""
    total_mail = 180
    mail_per_friend = 41
    mail_johann = total_mail - (2 * mail_per_friend)
    result = mail_johann
    return result

print(solution())