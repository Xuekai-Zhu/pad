def solution():
    
    total_dollars = 2 + 5
    total_quarters = 13
    total_dimes = 20
    total_nickels = 8
    total_pennies = 35
    total_cents = total_dollars*100 + total_quarters*25 + total_dimes*10 + total_nickels*5 + total_pennies
    total_money = total_cents / 100
    result = total_money
    return result

print(solution())