def solution():
    """Steve puts $100 into the bank. Each year he earns 10% interest on the money in the account. How much money will be in the bank after 2 years?"""
    initial_amount = 100
    interest_rate = 0.1
    time = 2
    final_amount = initial_amount * ((1 + interest_rate) ** time)
    result = final_amount
    return result

print(solution())