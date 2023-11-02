def solution():
    quarters = 4
    dimes = 6
    nickels = 9
    pennies = 5
    quarter_value = 25
    dime_value = 10
    nickel_value = 5
    penny_value = 1
    
    total_quarters = quarters * quarter_value
    total_dimes = dimes * dime_value
    total_nickels = nickels * nickel_value
    total_pennies = pennies * penny_value
    
    total_money = total_quarters + total_dimes + total_nickels + total_pennies
    
    return total_money

print(solution())