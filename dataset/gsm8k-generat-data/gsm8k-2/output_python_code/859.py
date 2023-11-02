def solution():
    """Earl has $90; Fred has $48; Greg has $36. Earl owes Fred $28. Fred owes Greg $32. Greg owes Earl $40. When all debts are paid, how much will Greg and Earl have together in dollars?"""
    earl_money = 90
    fred_money = 48
    greg_money = 36
    earl_owes_fred = 28
    fred_owes_greg = 32
    greg_owes_earl = 40
    # Subtract each debt from the appropriate person's total money
    earl_money -= earl_owes_fred + greg_owes_earl
    fred_money += earl_owes_fred - fred_owes_greg
    greg_money += fred_owes_greg - greg_owes_earl
    # Calculate total money for Greg and Earl
    total_money = earl_money + greg_money
    result = total_money
    return result

print(solution())