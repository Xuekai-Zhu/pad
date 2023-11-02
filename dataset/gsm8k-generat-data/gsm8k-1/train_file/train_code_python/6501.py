def solution():
    """Ivan has a piggy bank that can hold 100 pennies and 50 dimes. How much, in dollars, does Ivan have if he has filled his two piggy banks with those coins?"""
    pennies_per_bank = 100
    dimes_per_bank = 50
    total_pennies = pennies_per_bank * 2
    total_dimes = dimes_per_bank * 2
    total_cents = (total_pennies * 1) + (total_dimes * 10)
    total_dollars = total_cents / 100
    result = total_dollars
    return result

print(solution())