def solution():
    """Jake agrees to work part of his debt off. He owed someone $100 but paid them $40 before agreeing to work off the rest. He worked for $15 an hour. How many hours did he have to work?"""
    debt = 100
    paid_off = 40
    remaining_debt = debt - paid_off
    hourly_rate = 15
    hours_worked = remaining_debt / hourly_rate
    result = hours_worked
    
    return result

print(solution())