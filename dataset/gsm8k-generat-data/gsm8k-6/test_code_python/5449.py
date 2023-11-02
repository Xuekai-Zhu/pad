def solution():
    # Calculate the total number of houses that will receive junk mail
    total_houses = 8 - 2 - 3  # there are 8 houses, 2 have white mailboxes and 3 have red mailboxes, so 3 houses will receive junk mail

    # Calculate the number of pieces of junk mail each house will get
    mail_per_house = 48 / total_houses

    result = mail_per_house
    return result

print(solution())