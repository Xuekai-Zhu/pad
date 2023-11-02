def solution():
    """Margaux owns a money lending company. Her friend pays her $5 per day, her brother $8 per day, and her cousin $4 per day. How much money will she collect after 7 days?"""
    friend_payment = 5
    brother_payment = 8
    cousin_payment = 4
    days = 7
    total_money = (friend_payment + brother_payment + cousin_payment) * days
    result = total_money
    return result

print(solution())