def solution():
    """A person puts $5600 in a bank for two years. Each year he earns interest of 7% of the original amount deposited. How much will this person have in the bank after two years?"""
    initial_amount = 5600
    interest_rate = 0.07
    year_1_interest = initial_amount * interest_rate
    year_1_total = initial_amount + year_1_interest
    year_2_interest = year_1_total * interest_rate
    year_2_total = year_1_total + year_2_interest
    result = year_2_total
    return result

print(solution())