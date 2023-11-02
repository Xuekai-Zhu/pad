def solution():
    # Determine the number of pieces of mail sent on Tuesday and Wednesday
    tuesday_mail = 65 + 10
    wednesday_mail = tuesday_mail - 5

    # Determine the total number of pieces of mail sent
    total_mail = 65 + tuesday_mail + wednesday_mail + 15
    result = total_mail
    return result

print(solution())