def solution():
    total_mail = 180  # Johann and his friends need to deliver 180 pieces of mail
    friend_mail = 41  # Each of Johann's friends delivers 41 pieces of mail

    # Calculate the total pieces of mail Johann needs to deliver
    johann_mail = total_mail - (2 * friend_mail)

    result = johann_mail
    return result

print(solution())