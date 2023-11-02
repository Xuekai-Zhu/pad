def solution():
    total_mail = 180
    friends_mail = 41 * 2

    # Subtract the mail delivered by Johann's friends from the total mail to get the mail Johann needs to deliver
    johann_mail = total_mail - friends_mail
    result = johann_mail
    return result

print(solution())