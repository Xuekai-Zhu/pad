def solution():
    
    nickels = 20
    dimes = 3 * nickels
    additional_nickels = 2 * nickels
    total_nickels = nickels + additional_nickels
    total_money = (nickels * 0.05) + (dimes * 0.1) + (additional_nickels * 0.05)
    result = total_money
    return result

print(solution())