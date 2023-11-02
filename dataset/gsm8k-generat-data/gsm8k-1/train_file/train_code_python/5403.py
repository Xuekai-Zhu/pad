def solution():
    """Lauren sent 65 pieces of mail on Monday, 10 more pieces of mail on Tuesday than on Monday, 5 fewer on Wednesday than on Tuesday, and 15 more pieces of mail on Thursday than on Wednesday. How many pieces of mail did Lauren send?"""
    monday_mail = 65
    tuesday_mail = monday_mail + 10
    wednesday_mail = tuesday_mail - 5
    thursday_mail = wednesday_mail + 15
    total_mail = monday_mail + tuesday_mail + wednesday_mail + thursday_mail
    result = total_mail
    return result

print(solution())