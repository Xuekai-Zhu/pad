def solution():
    
    monday_mail = 65
    tuesday_mail = monday_mail + 10
    wednesday_mail = tuesday_mail - 5
    thursday_mail = wednesday_mail + 15
    total_mail = monday_mail + tuesday_mail + wednesday_mail + thursday_mail
    result = total_mail
    return result

print(solution())