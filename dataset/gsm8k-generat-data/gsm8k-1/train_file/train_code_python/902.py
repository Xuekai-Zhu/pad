def solution():
    """Margaux owns a money lending company. Her friend pays her $5 per day, her brother $8 per day, and her cousin $4 per day. How much money will she collect after 7 days?"""
    friend_payment = 5
    brother_payment = 8
    cousin_payment = 4
    num_days = 7
    friend_total = friend_payment * num_days
    brother_total = brother_payment * num_days
    cousin_total = cousin_payment * num_days
    total_collected = friend_total + brother_total + cousin_total
    result = total_collected
    return result

print(solution())