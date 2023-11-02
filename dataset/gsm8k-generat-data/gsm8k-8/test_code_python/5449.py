def solution():
    # Calculate the total number of houses that will receive junk mail
    total_houses = 8 - 2 - 3  # Subtract the number of houses with white and red mailboxes from the total number of houses

    # Calculate the number of junk mail pieces each house will receive
    mail_per_house = 48 / total_houses
    result = mail_per_house
    return result

print(solution())