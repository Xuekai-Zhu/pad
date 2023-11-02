def solution():
    
    candy_cost = 0.44
    paid_amount = 1
    change_amount = paid_amount - candy_cost
    quarters = int(change_amount/0.25)
    dimes = int((change_amount-quarters*0.25)/0.1)
    nickels = int((change_amount-quarters*0.25-dimes*0.1)/0.05)
    pennies = int((change_amount-quarters*0.25-dimes*0.1-nickels*0.05)/0.01)
    total_coins = quarters + dimes + nickels + pennies
    result = total_coins
    return result

print(solution())