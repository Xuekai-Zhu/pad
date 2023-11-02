def solution():
    initial_amount = 100  # initial amount deposited in the bank
    annual_interest_rate = 0.1  # 10% interest every year
    years = 2  # number of years
    final_amount = initial_amount * (1 + annual_interest_rate)**years  # final amount in the bank after 2 years
    result = final_amount
    return result

print(solution())