def solution():
    friend_pay = 5
    brother_pay = 8
    cousin_pay = 4
    num_days = 7

    # Calculate the total amount Margaux will collect from her friend
    friend_total = friend_pay * num_days

    # Calculate the total amount Margaux will collect from her brother
    brother_total = brother_pay * num_days

    # Calculate the total amount Margaux will collect from her cousin
    cousin_total = cousin_pay * num_days

    # Calculate the total amount Margaux will collect from all three individuals
    total_amount = friend_total + brother_total + cousin_total
    result = total_amount
    return result

print(solution())