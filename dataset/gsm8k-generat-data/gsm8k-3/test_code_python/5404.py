def solution():
    """Lauren sent 65 pieces of mail on Monday, 10 more pieces of mail on Tuesday than on Monday, 5 fewer on Wednesday than on Tuesday, and 15 more pieces of mail on Thursday than on Wednesday. How many pieces of mail did Lauren send?"""
    # Define the number of pieces of mail sent on Monday
    monday_mail = 65

    # Calculate the number of pieces of mail sent on Tuesday
    tuesday_mail = monday_mail + 10

    # Calculate the number of pieces of mail sent on Wednesday
    wednesday_mail = tuesday_mail - 5

    # Calculate the number of pieces of mail sent on Thursday
    thursday_mail = wednesday_mail + 15

    # Calculate the total number of pieces of mail sent
    total_mail = monday_mail + tuesday_mail + wednesday_mail + thursday_mail

    # Display the total number of pieces of mail sent
    result = total_mail
    return result

print(solution())