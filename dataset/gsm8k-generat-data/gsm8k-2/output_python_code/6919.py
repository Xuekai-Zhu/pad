def solution():
    """A person puts $5600 in a bank for two years. Each year he earns interest of 7% of the original amount deposited. How much will this person have in the bank after two years?"""
    amount = 5600
    rate = 0.07
    interest_1 = amount * rate
    balance_1 = amount + interest_1
    interest_2 = balance_1 * rate
    balance_2 = balance_1 + interest_2
    result = balance_2
    return result

print(solution())