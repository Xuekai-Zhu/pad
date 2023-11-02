def solution():
    
    dimes = 4
    quarters = 4 + 5
    nickels = 7
    total_cents = (dimes * 10) + (quarters * 25) + (nickels * 5)
    total_dollars = total_cents / 100
    result = total_dollars
    
    return result

print(solution())