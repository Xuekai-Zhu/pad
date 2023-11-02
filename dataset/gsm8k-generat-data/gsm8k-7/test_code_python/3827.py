def solution():
    twice_jericho_money = 60
    jericho_money = twice_jericho_money / 2
    annika_debt = 14
    manny_debt = annika_debt / 2
    
    # Calculate the total amount of debts Jericho has
    total_debt = annika_debt + manny_debt
    
    # Calculate how much money Jericho will have left after paying off all his debts
    money_left = jericho_money - total_debt
    result = money_left
    return result

print(solution())