def solution():
    """Earl has $90; Fred has $48; Greg has $36. Earl owes Fred $28. Fred owes Greg $32. Greg owes Earl $40. When all debts are paid, how much will Greg and Earl have together in dollars?"""
    # Calculate the net amount owed between Earl, Fred, and Greg
    net_earl = 90 - 28 - 40
    net_fred = 48 + 28 - 32
    net_greg = 36 + 32 + 40

    # Calculate the total amount of money after all debts are paid
    total_money = net_earl + net_fred + net_greg

    # Calculate the amount of money Greg and Earl will have together
    greg_and_earl_money = net_earl + net_greg

    # return the result
    result = greg_and_earl_money
    return result

print(solution())