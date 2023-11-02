def solution():
    # Determine how many pieces of mail Johann's friends delivered in total
    friends_mail_total = 41 * 2

    # Subtract the total mail delivered by Johann's friends from the total mail to be delivered
    johann_mail = 180 - friends_mail_total
    result = johann_mail
    return result

print(solution())