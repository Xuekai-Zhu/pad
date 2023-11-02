def solution():
    # Define the amount collected per day from each person
    friend_payment = 5
    brother_payment = 8
    cousin_payment = 4

    # Calculate the total amount collected after 7 days from each person
    friend_total = friend_payment * 7
    brother_total = brother_payment * 7
    cousin_total = cousin_payment * 7

    # Calculate the overall total collected after 7 days
    total_collected = friend_total + brother_total + cousin_total
    result = total_collected
    return result

print(solution())