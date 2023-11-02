def solution():
    """Earl has $90; Fred has $48; Greg has $36. Earl owes Fred $28. Fred owes Greg $32. Greg owes Earl $40. When all debts are paid, how much will Greg and Earl have together in dollars?"""
    # Calculate the net amount for each person
    earl_net = 90 - 28 + 40
    fred_net = 48 + 28 - 32
    greg_net = 36 + 32 - 40

    # Calculate the total amount that Greg and Earl have together
    total = earl_net + greg_net

    # Display the total amount
    result = total
    return result

print(solution())