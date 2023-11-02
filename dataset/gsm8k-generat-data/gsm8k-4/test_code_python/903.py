def solution():
    """Margaux owns a money lending company. Her friend pays her $5 per day, her brother $8 per day, and her cousin $4 per day. How much money will she collect after 7 days?"""
    # Define the amount each person will pay per day
    friend_payment = 5
    brother_payment = 8
    cousin_payment = 4

    # Calculate the total amount collected from each person after 7 days
    friend_total = friend_payment * 7
    brother_total = brother_payment * 7
    cousin_total = cousin_payment * 7

    # Calculate the total amount collected
    total_collected = friend_total + brother_total + cousin_total

    # return the result
    result = total_collected
    return result

print(solution())