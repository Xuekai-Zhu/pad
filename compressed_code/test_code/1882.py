def solution():
    
    nickels = 20
    new_nickels = 2 * nickels
    dimes = 3 * nickels
    total_nickels = nickels + new_nickels
    total_value = (total_nickels * 0.05) + (dimes * 0.1)
    result = total_value
    return result

print(solution())