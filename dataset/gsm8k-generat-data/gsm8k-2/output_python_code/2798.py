def solution():
    """Jake agrees to work part of his debt off. He owed someone $100 but paid them $40 before agreeing to work off the rest. He worked for $15 an hour. How many hours did he have to work?"""
    debt = 100
    paid = 40
    hours_worked = (debt - paid) / 15
    result = hours_worked
    return result

print(solution())