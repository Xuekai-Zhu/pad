def solution():
    initial_balance = 50.0
    interest_rate = 0.2  # 20% interest rate
    additional_charge = 20.0

    # Calculate the interest fee for the first month
    interest_fee_1 = initial_balance * interest_rate

    # Add the interest fee to the balance and the additional charge
    balance_1 = initial_balance + interest_fee_1 + additional_charge

    # Calculate the interest fee for the second month
    interest_fee_2 = balance_1 * interest_rate

    # Add the interest fee to the balance
    balance_2 = balance_1 + interest_fee_2
    result = balance_2
    return result

print(solution())