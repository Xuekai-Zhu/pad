def solution():
    """Earl has $90; Fred has $48; Greg has $36. Earl owes Fred $28. Fred owes Greg $32. Greg owes Earl $40. When all debts are paid, how much will Greg and Earl have together in dollars?"""
    earl = 90 - 28 + 40
    fred = 48 + 28 - 32
    greg = 36 + 32 - 40
    total = earl + greg
    result = total
    return result

print(solution())