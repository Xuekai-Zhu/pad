def solution():
    
    twice_jericho_money = 60
    jericho_money = twice_jericho_money / 2
    annika_debt = 14
    manny_debt = annika_debt / 2
    total_debt = annika_debt + manny_debt
    remaining_money = jericho_money - total_debt
    result = remaining_money
    return result

print(solution())