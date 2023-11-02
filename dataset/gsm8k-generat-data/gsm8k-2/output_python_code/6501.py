def solution():
    """Ivan has a piggy bank that can hold 100 pennies and 50 dimes. How much, in dollars, does Ivan have if he has filled his two piggy banks with those coins?"""
    pennies_per_piggy = 100
    dimes_per_piggy = 50
    total_pennies = pennies_per_piggy * 2
    total_dimes = dimes_per_piggy * 2
    total_value = (total_pennies * 0.01) + (total_dimes * 0.1)
    result = total_value
    return result

print(solution())