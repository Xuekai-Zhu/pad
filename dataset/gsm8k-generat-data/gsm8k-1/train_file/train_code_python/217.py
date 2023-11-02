def solution():
    """Ravi has some coins. He has 2 more quarters than nickels and 4 more dimes than quarters. If he has 6 nickels, how much money does he have?"""
    num_nickels = 6
    num_quarters = num_nickels + 2
    num_dimes = num_quarters + 4
    
    value_nickels = num_nickels * 0.05
    value_quarters = num_quarters * 0.25
    value_dimes = num_dimes * 0.10
    
    total_value = value_nickels + value_quarters + value_dimes
    result = total_value
    return result

print(solution())