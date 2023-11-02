def solution():
    
    quarter_value = 0.25
    nickel_value = 0.05
    dime_value = 0.10
    num_quarter = 1
    num_nickels = 2
    num_dimes = 7
    total_value = (quarter_value * num_quarter) + (nickel_value * num_nickels) + (dime_value * num_dimes)
    result = total_value
    return result

print(solution())