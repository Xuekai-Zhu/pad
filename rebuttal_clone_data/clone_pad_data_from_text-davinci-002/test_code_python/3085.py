def solution():
    pennies = 120
    nickels = pennies / 3
    dimes = nickels / 5
    quarters = dimes * 2
    total = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25)
    result = total
    return result

print(solution())