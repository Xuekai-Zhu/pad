def solution():
    
    quarters = 8
    dimes = 6
    nickels = 14
    pennies = 15
    total_quarters = quarters * 25
    total_dimes = dimes * 10
    total_nickels = nickels * 5
    total_pennies = pennies * 1
    total_price = total_quarters + total_dimes + total_nickels + total_pennies
    result = total_price
    return result

print(solution())