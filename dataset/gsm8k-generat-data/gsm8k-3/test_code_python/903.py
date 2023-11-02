def solution():
    """Margaux owns a money lending company. Her friend pays her $5 per day, her brother $8 per day, and her cousin $4 per day. How much money will she collect after 7 days?"""
    
    # Define the amount of money collected per day from each person
    friend_pay = 5
    brother_pay = 8
    cousin_pay = 4

    # Define the number of days each person is borrowing money
    friend_days = 7
    brother_days = 7
    cousin_days = 7

    # Calculate the total amount of money collected
    total = (friend_pay * friend_days) + (brother_pay * brother_days) + (cousin_pay * cousin_days)

    # Display the total amount of money collected
    result = total
    return result

print(solution())