def solution():
    
    pennies_per_piggy = 100
    dimes_per_piggy = 50
    total_pennies = pennies_per_piggy * 2
    total_dimes = dimes_per_piggy * 2
    total_value = (total_pennies * 0.01) + (total_dimes * 0.1)
    result = total_value
    return result

print(solution())