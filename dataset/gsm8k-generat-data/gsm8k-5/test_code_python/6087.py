def solution():
    principal = 100  # The initial amount Steve puts into the bank
    rate = 0.1  # The interest rate is 10%
    years = 2  # Steve wants to know how much money will be in the bank after 2 years

    # Calculate the amount of money in the bank after 2 years with compound interest
    amount = principal * (1 + rate) ** years

    result = amount
    return result

print(solution())