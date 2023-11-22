def solution():
    
    pennies = 100
    nickels = 40
    dimes = 20
    dollar_bills = 40
    total_money = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (dollar_bills * 0.01)
    result = total_money
    return result

print(solution())