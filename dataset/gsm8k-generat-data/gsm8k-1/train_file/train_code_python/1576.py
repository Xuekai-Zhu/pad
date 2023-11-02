def solution():
    """Steve has a bank account that earns 10% interest every year. He puts $100 in it, and then 10 each year. How much money is in it after two years?"""
    initial_deposit = 100
    annual_contribution = 10
    interest_rate = 0.1
    year_one_balance = initial_deposit * (1 + interest_rate) + annual_contribution
    year_two_balance = year_one_balance * (1 + interest_rate) + annual_contribution
    result = year_two_balance
    return result

print(solution())