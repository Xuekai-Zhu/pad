def solution():
    cost_of_candy = 0.44
    amount_paid = 1.00
    change_due = amount_paid - cost_of_candy
    quarters = int(change_due / 0.25)
    dimes = int((change_due - (quarters * 0.25)) / 0.10)
    nickels = int((change_due - ((quarters * 0.25) + (dimes * 0.10))) / 0.05)
    pennies = int((change_due - ((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05))) / 0.01)
    total_coins = quarters + dimes + nickels + pennies
    result = total_coins
    return result

print(solution())